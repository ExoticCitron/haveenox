import json

def parse_json(json_string):
    """
    Parses a JSON string into a Python dictionary.
    
    Args:
        json_string (str): The JSON string to parse.
    
    Returns:
        dict: A Python dictionary representing the parsed JSON data.
    """
    try:
        parsed_data = json.loads(json_string)
        return parsed_data
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return {}
