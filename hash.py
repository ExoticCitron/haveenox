import bcrypt

def hash(password, salt_rounds=12):
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to hash.
        salt_rounds (int, optional): The number of salt rounds. Defaults to 12.

    Returns:
        str: The hashed password.
    """
    # Generate salt and hash the password
    salt = bcrypt.gensalt(rounds=salt_rounds)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


print("Hashed Password:", hashed_password)
