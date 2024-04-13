import requests
import json

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
        return f"{response}"
    else:
        print(f"Failed to post message to Discord. Status code: {response.status_code}")
        return None
