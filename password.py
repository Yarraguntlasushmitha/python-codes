import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        for _ in range(num_passwords):
            password = generate_password(password_length)
            print("Generated Password:", password)

    except ValueError:
        print("Please enter valid numeric values for password length and number of passwords.")

if __name__ == "__main__":
    main()
