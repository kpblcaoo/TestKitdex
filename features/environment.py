"""
Behave environment configuration for TestKit indexing tests.
"""

import os
import tempfile
import shutil
from pathlib import Path


def before_scenario(context, scenario):
    """Setup before each scenario."""
    # Create temporary directory for test files
    context.temp_dir = tempfile.mkdtemp()
    context.test_dir = Path(context.temp_dir)
    
    # Create clean database path
    context.db_path = os.path.join(context.temp_dir, "testkit_test.db")
    
    # Initialize test data
    context.test_files = []
    context.indexer = None


def after_scenario(context, scenario):
    """Cleanup after each scenario."""
    # Clean up temporary directory
    if hasattr(context, 'temp_dir') and os.path.exists(context.temp_dir):
        shutil.rmtree(context.temp_dir)
    
    # Clean up test files
    for file_path in getattr(context, 'test_files', []):
        if os.path.exists(file_path):
            os.remove(file_path) 