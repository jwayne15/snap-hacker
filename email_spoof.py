import smtplib
import getpass

# Gmail SMTP server settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Gmail account credentials
ACCOUNT_EMAIL = input("Enter the Gmail account email: ")
ACCOUNT_PASSWORD = getpass.getpass("Enter the Gmail account password: ")

def email_spoofing():
    sender_email = input("Enter the spoofed email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")
    
    message = f"From: {sender_email}\nTo: {ACCOUNT_EMAIL}\nSubject: {subject}\n\n{body}"
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(ACCOUNT_EMAIL, ACCOUNT_PASSWORD)
        server.sendmail(sender_email, ACCOUNT_EMAIL, message)
        print("Spoofed email sent successfully.")
        server.quit()
    except Exception as e:
        print(f"Failed to send spoofed email: {e}")
