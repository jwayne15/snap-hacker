from brute_force import brute_force_login
from snapchat_spoof import snapchat_spoofing
from password_strength import password_strength_tester

def main():
    print("Snapchat Pentester Tool")
    print("--------------------")
    print("1. Brute-Force Login")
    print("2. snapchat Spoofing")
    print("3. Password Strength Tester")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        brute_force_login()
    elif choice == "2":
        snapchat_spoofing()
    elif choice == "3":
        password_strength_tester()
    elif choice == "4":
        print("Goodbye")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
