# Resolve the problem!!
import string
import random


SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S,' 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'Y', 'z']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def generate_password():

    ALL = UPPERCASE + LOWERCASE + NUMBERS + SYMBOLS
    password = []
    length = random.randint(8,16)

    for i in range(length):
        if i == 0:
            caracter_random = random.choice(SYMBOLS)
            password.append(caracter_random)
        elif i == 1:
            caracter_random = random.choice(UPPERCASE)
            password.append(caracter_random)
        elif i == 2:
            caracter_random = random.choice(LOWERCASE)
            password.append(caracter_random)
        elif i == 3: 
            caracter_random = random.choice(NUMBERS)
            password.append(caracter_random)
        else:
            caracter_random = random.choice(ALL)
            password.append(caracter_random)

    password = ''.join(password)
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
