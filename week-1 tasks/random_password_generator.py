import argparse
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    if not any([use_uppercase, use_lowercase, use_digits, use_special]):
        raise ValueError("At least one character type must be selected")

    char_pool = ''
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Random Password Generator')
    parser.add_argument('-l', '--length', type=int, required=True, help='Length of the password')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-lo', '--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--special', action='store_true', help='Include special characters')

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_uppercase=args.uppercase,
            use_lowercase=args.lowercase,
            use_digits=args.digits,
            use_special=args.special
        )
        print(f'Generated password: {password}')
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
