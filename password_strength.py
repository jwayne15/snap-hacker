import getpass

# Gmail account credentials
ACCOUNT_PASSWORD = getpass.getpass("Enter the Gmail account password: ")

def password_strength_tester():
    password = ACCOUNT_PASSWORD
    strength = 0
    
    if len(password) < 8:
        print("Password is too short")
    elif not any(char.isdigit() for char in password):
        print("Password should have at least one digit")
    elif not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter")
    elif not any(char.islower() for char in password):
        print("Password should have at least one lowercase letter")
    else:
        strength += 1
    
    if strength == 1:
        print("Password is strong")
    else:
        print("Password is weak")
