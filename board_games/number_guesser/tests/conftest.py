"""
Pytest configuration file
"""

import pytest
import sys
import os

# Add the src directory to Python path
# This allows imports from the src directory to work in the tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
