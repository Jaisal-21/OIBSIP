import string


def check_password_strength(password):
    """
    Returns:
        ("Weak", "red")
        ("Medium", "orange")
        ("Strong", "green")
    """

    if not password:
        return "Weak", "red"

    score = 0

    # Length
    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    # Character Types
    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    # Final Rating
    if score <= 2:
        return "Weak", "red"

    elif score <= 4:
        return "Medium", "orange"

    else:
        return "Strong", "green"