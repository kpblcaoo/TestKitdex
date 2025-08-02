"""
Database models for TestKit indexer.
"""
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from typing import List, Optional

Base = declarative_base()

# Association table for many-to-many relationship between methods and tags
method_tags = Table(
    'method_tags',
    Base.metadata,
    Column('method_id', Integer, ForeignKey('methods.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Method(Base):
    """Database model for C# methods."""
    
    __tablename__ = 'methods'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, index=True)
    return_type = Column(String(100), nullable=False)
    signature = Column(String(500), nullable=False)
    full_signature = Column(String(1000), nullable=False)
    summary = Column(Text)
    is_static = Column(Boolean, default=False)
    is_generic = Column(Boolean, default=False)
    is_public = Column(Boolean, default=True)
    file_path = Column(String(500))
    line_number = Column(Integer)
    
    # Relationships
    tags = relationship("Tag", secondary=method_tags, back_populates="methods")
    parameters = relationship("Parameter", back_populates="method", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Method(name='{self.name}', return_type='{self.return_type}')>"


class Tag(Base):
    """Database model for method tags."""
    
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(Text)
    
    # Relationships
    methods = relationship("Method", secondary=method_tags, back_populates="tags")
    
    def __repr__(self):
        return f"<Tag(name='{self.name}')>"


class Parameter(Base):
    """Database model for method parameters."""
    
    __tablename__ = 'parameters'
    
    id = Column(Integer, primary_key=True)
    method_id = Column(Integer, ForeignKey('methods.id'), nullable=False)
    name = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)
    default_value = Column(String(255))
    position = Column(Integer, nullable=False)
    
    # Relationships
    method = relationship("Method", back_populates="parameters")
    
    def __repr__(self):
        return f"<Parameter(name='{self.name}', type='{self.type}')>"


class SearchIndex(Base):
    """FTS5 virtual table for full-text search."""
    
    __tablename__ = 'search_index'
    
    # FTS5 virtual table columns
    id = Column(Integer, primary_key=True)
    method_name = Column(String(255))
    method_summary = Column(Text)
    tags_text = Column(Text)
    signature_text = Column(Text)
    
    def __repr__(self):
        return f"<SearchIndex(method_name='{self.method_name}')>" 