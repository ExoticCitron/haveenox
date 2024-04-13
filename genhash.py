import random
import string
import secrets
import hashlib
import bcrypt

def generate_password(length=12, include_symbols=True):
    """
    Generates a random password of specified length with optional inclusion of symbols.

    Args:
        length (int, optional): Length of the password. Defaults to 12.
        include_symbols (bool, optional): Whether to include symbols in the password. Defaults to True.

    Returns:
        str: A randomly generated password.
    """
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def hash_password(password, algorithm='sha256'):
    """
    Hashes a password using the specified hashing algorithm.

    Args:
        password (str): The password to hash.
        algorithm (str, optional): The hashing algorithm to use (e.g., 'sha256', 'md5'). Defaults to 'sha256'.

    Returns:
        str: The hashed password.
    """
    if algorithm == 'sha256':
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'md5':
        hashed_password = hashlib.md5(password.encode()).hexdigest()
    else:
        raise ValueError("Invalid hashing algorithm. Supported algorithms: 'sha256', 'md5'")
    return hashed_password

def hash_password_bcrypt(password, salt_rounds=12):
    """
    Hashes a password using the bcrypt algorithm.

    Args:
        password (str): The password to hash.
        salt_rounds (int, optional): The number of salt rounds to use. Defaults to 12.

    Returns:
        str: The hashed password.
    """
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt(salt_rounds)).decode()
    return hashed_password

# Test the functions

password = generate_password()
print("Generated Password:", password)

hashed_password = hash_password(password)
print("Hashed Password (SHA-256):", hashed_password)

hashed_password_bcrypt = hash_password_bcrypt(password)
print("Hashed Password (BCrypt):", hashed_password_bcrypt)
