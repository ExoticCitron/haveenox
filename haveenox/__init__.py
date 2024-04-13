# __init__.py

# Define the color codes and names
COLORS = {
    'GREEN': '\033[92m',
    'RED': '\033[91m',
    'YELLOW': '\033[93m',
    # Add more colors as needed
    'RESET': '\033[0m'
}

# Dynamically create the color variables
for color_name, color_code in COLORS.items():
    globals()[color_name] = color_code

from .haveenox import *
