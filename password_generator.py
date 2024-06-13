import random
import string

def generate_password(length):
    char_pool = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
