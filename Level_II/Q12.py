# Q12.py
def login_system():
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")
        retype_password = input("Re-type password: ")
        if password == retype_password:
            return "Registration successful!"
        else:
            attempts += 1
            print(f"Passwords do not match. You have {max_attempts - attempts} attempt(s) left.")
    return "Registration failed. Too many attempts."

# Example usage
if __name__ == "__main__":
    print(login_system())
