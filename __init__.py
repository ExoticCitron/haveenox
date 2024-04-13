import os

RESET = '\033[0m'
BLACK = '\033[30m' 
RED = '\033[31m'
GREEN = '\033[32m' 
YELLOW = '\033[33m'
BLUE = '\033[34m' 
MAGENTA = '\033[35m' 
CYAN = '\033[36m' 
WHITE = '\033[37m' 
LIGHTBLACK = '\033[90m' 
LIGHTRED = '\033[91m' 
LIGHTGREEN = '\033[92m' 
LIGHTYELLOW = '\033[93m' 
LIGHTBLUE = '\033[94m' 
LIGHTMAGENTA = '\033[95m' 
LIGHTCYAN = '\033[96m' 
LIGHTWHITE = '\033[97m' 

def clr():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def repeat(string, times):
    """Repeats the given string a set number of times."""
    if not isinstance(string, str):
        print(RED + "Error: The first argument must be a string." + RESET)
        return
    if not isinstance(times, int):
        print(RED + "Error: The second argument must be an integer." + RESET)
        return
    for _ in range(times):
        print(string)
