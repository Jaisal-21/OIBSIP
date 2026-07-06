import secrets
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """
    Generate a secure random password based on user preferences.
    """

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    # Return None if no character type is selected
    if not characters:
        return None

    password = "".join(secrets.choice(characters) for _ in range(length))

    return password