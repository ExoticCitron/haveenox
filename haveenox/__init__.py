# __init__.py

# Define ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
# Add more colors as needed
RESET = '\033[0m'

# Import everything from haveenox.py
from .haveenox import *

# Alternatively, you can specify exactly what you want to import:
# from .haveenox import GREEN, RED, YELLOW, RESET
