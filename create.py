import json

def create(file_name, mode=None, content=None):
    """
    Opens or creates a file and performs specified actions.

    Args:
        file_name (str): The name of the file to open or create.
        mode (str, optional): The mode in which to open the file ('r' for reading, 'w' for writing, 'a' for appending).
        content (str or dict, optional): The content to write to the file. Default is None.

    Returns:
        str: The content read from the file (if mode is 'r'), or None otherwise.
    """
    try:
        if mode is None:
            mode = 'r'
        with open(file_name, mode) as file:
            if mode == 'r':
                file_content = file.read()
                if file_content:
                    print(file_content)
                else:
                    print("File is empty.")
                return file_content
            elif mode == 'w':
                if content is not None:
                    file.write(content)
                    print(f"Content '{content}' written to '{file_name}'.")
                else:
                    print("No content provided to write.")
            elif mode == 'a':
                if content is not None:
                    file.write(content)
                    print(f"Content '{content}' appended to '{file_name}'.")
                else:
                    print("No content provided to append.")
            else:
                print(f"\033[31mInvalid mode '{mode}'. Please use 'r', 'w', or 'a'.\033[0m")
    except FileNotFoundError:
        print(f"\033[31mFile '{file_name}' not found. Creating a new file...\033[0m")
        with open(file_name, 'w') as file:
            if content is not None:
                if isinstance(content, dict):
                    try:
                        json.dump(content, file, indent=4)
                        print(f"JSON content written to '{file_name}'.")
                    except Exception as e:
                        print(f"\033[31mError writing JSON content: {e}\033[0m")
                else:
                    file.write(content)
                    print(f"Content '{content}' written to '{file_name}'.")
            else:
                print("No content provided to write.")
    except Exception as e:
        print(f"\033[31mError occurred: {e}\033[0m")
