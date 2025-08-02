"""
Database repository for TestKit indexer.
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional, Dict, Any
from .models import Base, Method, Tag, Parameter, SearchIndex
from ..parser.models import CSharpMethod


class TestKitRepository:
    """Repository for TestKit database operations."""
    
    def __init__(self, database_url: str = "sqlite:///testkit.db"):
        """Initialize repository with database URL."""
        self.engine = create_engine(database_url, echo=False)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
    def create_tables(self):
        """Create all database tables."""
        Base.metadata.create_all(bind=self.engine)
        
        # Create FTS5 virtual table
        with self.engine.connect() as conn:
            conn.execute(text("""
                CREATE VIRTUAL TABLE IF NOT EXISTS search_index 
                USING fts5(id, method_name, method_summary, tags_text, signature_text)
            """))
            conn.commit()
        
    def get_session(self) -> Session:
        """Get database session."""
        return self.SessionLocal()
    
    def store_method(self, method: CSharpMethod) -> Method:
        """
        Store a C# method in the database.
        
        Args:
            method: CSharpMethod object to store
            
        Returns:
            Stored Method object
        """
        with self.get_session() as session:
            try:
                # Create or get tags
                tags = []
                for tag_name in method.tags:
                    tag = session.query(Tag).filter(Tag.name == tag_name).first()
                    if not tag:
                        tag = Tag(name=tag_name)
                        session.add(tag)
                    tags.append(tag)
                
                # Create method
                db_method = Method(
                    name=method.name,
                    return_type=method.return_type,
                    signature=method.signature,
                    full_signature=method.full_signature,
                    summary=method.summary,
                    is_static=method.is_static,
                    is_generic=method.is_generic,
                    is_public=method.is_public,
                    file_path=method.file_path,
                    line_number=method.line_number,
                    tags=tags
                )
                
                session.add(db_method)
                session.flush()  # Flush to get the ID
                
                # Add parameters
                for i, param_str in enumerate(method.parameters):
                    # Parse parameter string (e.g., "string name = \"TestUser\"")
                    param_parts = param_str.split('=', 1)
                    param_name_type = param_parts[0].strip()
                    
                    # Extract name and type
                    if ' ' in param_name_type:
                        param_type, param_name = param_name_type.rsplit(' ', 1)
                    else:
                        param_type = param_name_type
                        param_name = f"param_{i}"
                    
                    default_value = param_parts[1].strip().strip('"') if len(param_parts) > 1 else None
                    
                    parameter = Parameter(
                        method=db_method,
                        name=param_name,
                        type=param_type,
                        default_value=default_value,
                        position=i
                    )
                    session.add(parameter)
                
                session.commit()
                
                # Return a fresh object with loaded relationships
                return session.query(Method).filter(Method.id == db_method.id).first()
                
            except SQLAlchemyError as e:
                session.rollback()
                raise Exception(f"Failed to store method: {e}")
    
    def get_method_by_name(self, name: str) -> Optional[Method]:
        """
        Get method by name.
        
        Args:
            name: Method name
            
        Returns:
            Method object or None
        """
        with self.get_session() as session:
            return session.query(Method).filter(Method.name == name).first()
    
    def get_methods_by_tags(self, tags: List[str]) -> List[Method]:
        """
        Get methods by tags.
        
        Args:
            tags: List of tag names
            
        Returns:
            List of Method objects
        """
        with self.get_session() as session:
            return session.query(Method).join(Method.tags).filter(
                Tag.name.in_(tags)
            ).all()
    
    def get_all_methods(self) -> List[Method]:
        """Get all methods."""
        with self.get_session() as session:
            return session.query(Method).all()
    
    def get_all_tags(self) -> List[Tag]:
        """Get all tags."""
        with self.get_session() as session:
            return session.query(Tag).all()
    
    def search_methods(self, query: str) -> List[Method]:
        """
        Search methods using FTS5.
        
        Args:
            query: Search query
            
        Returns:
            List of matching Method objects
        """
        with self.get_session() as session:
            # Use FTS5 search
            search_query = text("""
                SELECT m.id FROM methods m
                JOIN search_index si ON m.id = si.id
                WHERE search_index MATCH :query
                ORDER BY rank
            """)
            
            result = session.execute(search_query, {"query": query})
            method_ids = [row[0] for row in result]
            
            if method_ids:
                return session.query(Method).filter(Method.id.in_(method_ids)).all()
            return []
    
    def update_search_index(self):
        """Update FTS5 search index."""
        with self.get_session() as session:
            # Clear existing index
            session.execute(text("DELETE FROM search_index"))
            
            # Rebuild index
            methods = session.query(Method).all()
            for method in methods:
                tags_text = " ".join([tag.name for tag in method.tags])
                signature_text = f"{method.name} {method.signature}"
                
                search_entry = SearchIndex(
                    id=method.id,
                    method_name=method.name,
                    method_summary=method.summary or "",
                    tags_text=tags_text,
                    signature_text=signature_text
                )
                session.add(search_entry)
            
            session.commit()
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics."""
        with self.get_session() as session:
            method_count = session.query(Method).count()
            tag_count = session.query(Tag).count()
            parameter_count = session.query(Parameter).count()
            
            # Get top tags
            top_tags = session.execute(text("""
                SELECT t.name, COUNT(*) as count
                FROM tags t
                JOIN method_tags mt ON t.id = mt.tag_id
                GROUP BY t.id, t.name
                ORDER BY count DESC
                LIMIT 10
            """)).fetchall()
            
            return {
                "method_count": method_count,
                "tag_count": tag_count,
                "parameter_count": parameter_count,
                "top_tags": [{"name": tag[0], "count": tag[1]} for tag in top_tags]
            } 