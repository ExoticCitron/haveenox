import os
import json

# Color codes
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

# Try to import requests module
try:
    import requests
except ImportError:
    # If not found, try to install it
    print(YELLOW + "Installing 'requests' module..." + RESET)
    os.system('pip install requests')

    # Try to import requests again
    try:
        import requests
    except ImportError:
        print(RED + "Error: Failed to install 'requests' module. Please install it manually using 'pip install requests'." + RESET)

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

def dcPost(url, content):
    """
    Posts content to a Discord webhook.
    
    Args:
        url (str): The URL of the Discord webhook.
        content (str): The content to be posted.
    
    Returns:
        Coroutine object with the content sent, or None if the posting failed.
    """
    data = {
        "content": content
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    if response.status_code == 204:
        print("Message posted successfully to Discord.")
        print(f"<coroutine Object 'sent-{content}'>") 
    else:
        print(f"Failed to post message to Discord. Status code: {response.status_code}")
        return None
