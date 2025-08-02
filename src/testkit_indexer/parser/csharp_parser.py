"""
C# parser for extracting methods with tags from TestKit files.
"""
import re
from typing import List, Optional
from .models import CSharpMethod, ParseResult


class CSharpParser:
    """Parser for C# files to extract methods with XML documentation tags."""
    
    def __init__(self):
        """Initialize the parser."""
        # Regex patterns for parsing
        self.method_pattern = re.compile(
            r'(?:public\s+)?(?:static\s+)?(\w+(?:<[^>]+>)?)\s+(\w+(?:<[^>]+>)?)\s*\([^)]*\)\s*(?:where\s+[^{]*)?\s*\{',
            re.MULTILINE
        )
        self.xml_doc_pattern = re.compile(
            r'///\s*<summary>\s*(.*?)\s*</summary>',
            re.DOTALL
        )
        self.tags_pattern = re.compile(
            r'<tags>(.*?)</tags>',
            re.DOTALL
        )
        self.static_pattern = re.compile(r'\bstatic\b')
        self.generic_pattern = re.compile(r'<[^>]+>')
        self.public_pattern = re.compile(r'\bpublic\b')

    def extract_methods(self, code: str, file_path: Optional[str] = None) -> List[CSharpMethod]:
        """
        Extract methods from C# code.
        
        Args:
            code: C# source code as string
            file_path: Optional file path for context
            
        Returns:
            List of CSharpMethod objects
        """
        methods = []
        
        try:
            # Find all method declarations
            for match in self.method_pattern.finditer(code):
                return_type = match.group(1)
                method_name = match.group(2)
                
                # Get the method signature line
                method_line = match.group(0)
                
                # Extract XML documentation if present
                summary, tags = self._extract_xml_documentation(code, match.start())
                
                # Determine method properties
                is_static = bool(self.static_pattern.search(method_line))
                is_generic = bool(self.generic_pattern.search(method_name))
                is_public = bool(self.public_pattern.search(method_line))
                
                # Clean method name from generic parameters
                clean_method_name = self._clean_generic_name(method_name)
                
                # Create method object
                method = CSharpMethod(
                    name=clean_method_name,
                    return_type=return_type,
                    parameters=self._extract_parameters(method_line),
                    tags=tags,
                    summary=summary,
                    is_static=is_static,
                    is_generic=is_generic,
                    is_public=is_public,
                    file_path=file_path,
                    line_number=self._get_line_number(code, match.start())
                )
                
                methods.append(method)
                
        except Exception as e:
            # Log error but continue processing
            print(f"Error parsing code: {e}")
            
        return methods

    def parse_file(self, file_path: str) -> ParseResult:
        """
        Parse a C# file and extract methods.
        
        Args:
            file_path: Path to the C# file
            
        Returns:
            ParseResult with extracted methods
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            methods = self.extract_methods(code, file_path)
            return ParseResult(methods=methods, file_path=file_path)
            
        except Exception as e:
            return ParseResult(
                methods=[],
                file_path=file_path,
                success=False,
                errors=[str(e)]
            )

    def _extract_xml_documentation(self, code: str, method_start: int) -> tuple[Optional[str], List[str]]:
        """
        Extract XML documentation from before the method.
        
        Args:
            code: Full source code
            method_start: Position where method starts
            
        Returns:
            Tuple of (summary, tags)
        """
        # Look for XML documentation before the method
        before_method = code[:method_start]
        
        # Find the last XML documentation block
        summary_match = None
        for match in self.xml_doc_pattern.finditer(before_method):
            summary_match = match
        
        if not summary_match:
            return None, []
        
        summary = summary_match.group(1).strip()
        
        # Extract tags from the XML documentation
        tags = []
        tags_match = self.tags_pattern.search(summary_match.group(0))
        if tags_match:
            tags_text = tags_match.group(1).strip()
            tags = [tag.strip() for tag in tags_text.split(',') if tag.strip()]
        
        return summary, tags

    def _extract_parameters(self, method_line: str) -> List[str]:
        """
        Extract parameter list from method signature.
        
        Args:
            method_line: Method signature line
            
        Returns:
            List of parameter strings
        """
        # Find parameters between parentheses
        param_match = re.search(r'\(([^)]*)\)', method_line)
        if not param_match:
            return []
        
        params_text = param_match.group(1).strip()
        if not params_text:
            return []
        
        # Split by comma and clean up
        params = []
        for param in params_text.split(','):
            param = param.strip()
            if param:
                params.append(param)
        
        return params

    def _clean_generic_name(self, name: str) -> str:
        """
        Clean generic type parameters from method name.
        
        Args:
            name: Method name with possible generic parameters
            
        Returns:
            Clean method name without generic parameters
        """
        # Remove generic type parameters like <T> or <T, U>
        return re.sub(r'<[^>]+>', '', name)

    def _get_line_number(self, code: str, position: int) -> int:
        """
        Get line number for a position in code.
        
        Args:
            code: Source code
            position: Character position
            
        Returns:
            Line number (1-based)
        """
        return code[:position].count('\n') + 1 