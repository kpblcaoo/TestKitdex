"""
Data models for C# parser.
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CSharpMethod:
    """Represents a C# method with metadata."""
    
    name: str
    return_type: str
    parameters: List[str]
    tags: List[str]
    summary: Optional[str] = None
    is_static: bool = False
    is_generic: bool = False
    is_public: bool = True
    file_path: Optional[str] = None
    line_number: Optional[int] = None
    
    def __post_init__(self):
        """Validate method data after initialization."""
        if not self.name:
            raise ValueError("Method name cannot be empty")
        if not self.return_type:
            raise ValueError("Return type cannot be empty")
        
        # Normalize tags
        self.tags = [tag.strip().lower() for tag in self.tags if tag.strip()]
        
        # Normalize parameters
        self.parameters = [param.strip() for param in self.parameters if param.strip()]

    @property
    def signature(self) -> str:
        """Get method signature."""
        params = ", ".join(self.parameters) if self.parameters else ""
        return f"{self.name}({params})"

    @property
    def full_signature(self) -> str:
        """Get full method signature with return type."""
        static = "static " if self.is_static else ""
        return f"{static}{self.return_type} {self.signature}"

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "return_type": self.return_type,
            "parameters": self.parameters,
            "tags": self.tags,
            "summary": self.summary,
            "is_static": self.is_static,
            "is_generic": self.is_generic,
            "is_public": self.is_public,
            "file_path": self.file_path,
            "line_number": self.line_number,
            "signature": self.signature,
            "full_signature": self.full_signature,
        }


@dataclass
class ParseResult:
    """Result of parsing a C# file."""
    
    methods: List[CSharpMethod]
    file_path: str
    success: bool = True
    errors: List[str] = None
    
    def __post_init__(self):
        """Initialize errors list if not provided."""
        if self.errors is None:
            self.errors = []

    @property
    def method_count(self) -> int:
        """Get number of methods found."""
        return len(self.methods)

    @property
    def tag_count(self) -> int:
        """Get total number of unique tags."""
        all_tags = set()
        for method in self.methods:
            all_tags.update(method.tags)
        return len(all_tags) 