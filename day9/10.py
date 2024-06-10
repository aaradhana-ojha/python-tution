def is_valid_password(password):
    """
    Checks if the provided password meets the following requirements:

    - At least eight characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one numeric digit

    Provides informative feedback on any failed conditions.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """

    min_length = 8
    uppercase_found = False
    lowercase_found = False
    digit_found = False

    if len(password) < min_length:
        print(f"Password is too short. It must be at least {min_length} characters long.")
        return False

    for char in password:
        if char.isupper():
            uppercase_found = True
        elif char.islower():
            lowercase_found = True
        elif char.isdigit():
            digit_found = True

    if not uppercase_found:
        print("Password must contain at least one uppercase letter.")
    if not lowercase_found:
        print("Password must contain at least one lowercase letter.")
    if not digit_found:
        print("Password must contain at least one numeric digit.")

    return uppercase_found and lowercase_found and digit_found

password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Please address the mentioned issues.")
