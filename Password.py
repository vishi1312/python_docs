print("*** Hello CognoRise ***")

print("       {{Task 2}}      ")

print("---------------------------------- \n Welcome to Password Generator... \n ----------------------------------")

import random
import string

def generate_password(length):
    # Define the characters to choose from for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password is:", password)

if __name__ == "__main__":
    main()
