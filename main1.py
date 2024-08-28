from brute_force import brute_force_login
from email_spoof import email_spoofing
from password_strength import password_strength_tester

def main():
    print("Gmail Pentester Tool")
    print("--------------------")
    print("1. Brute-Force Login")
    print("2. Email Spoofing")
    print("3. Password Strength Tester")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        brute_force_login()
    elif choice == "2":
        email_spoofing()
    elif choice == "3":
        password_strength_tester()
    elif choice == "4":
        print("Goodbye")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
