def greet_user(username):
    """ Displays the name of the user."""
    if not isinstance(username, str):
        raise TypeError("Username must be a string.")
    if not username.strip():
        raise ValueError("Username cannot be empty.")
    print(f"Hello, {username.title()}!")

try:
    greet_user('Maria') 
except TypeError as e:
    print(f"Type Error: {e}")
except ValueError as e:
    print(f"Value Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")