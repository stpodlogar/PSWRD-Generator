import secrets
import string

def generate_pwd():
    print('\nWelcome to PSWRD Generator')
    print('=' * 26 + '\n')

    #get user input for length of password to generate
    length = int(input('Please enter the desired password length: '))

    #define data
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = '!@#$%^&*'

    #combine data
    chars = lower + upper + num + symbols

    #generate array of random chars
    temp = (secrets.choice(chars) for char in range(length))

    #combine temp array to create password
    password = ''.join(temp)

    print(f'\n{password}\n')

generate_pwd()