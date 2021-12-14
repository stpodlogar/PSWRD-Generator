import secrets
import string
import random
import array

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
    #combine all characters
    chars = lower + upper + num + symbols

    #get minimum number of digits and special chars from user
    num_digits = int(input('Minimum numbers: '))
    num_special = int(input('Minimum special characters: '))
    #initialize the required number or specific characters
    rand_digit = str()
    rand_special = str()
    rand_upper = (secrets.choice(upper))
    rand_lower = (secrets.choice(lower))

    for _ in range(num_digits):
        rand_digit += secrets.choice(num)

    for _ in range(num_special):
        rand_special += secrets.choice(symbols)

    temp_pass = rand_digit + rand_special + rand_upper + rand_lower

    for _ in range(length - (num_digits + num_special + 2)):
        temp_pass += secrets.choice(chars)

    #convert tmp_pass to list and shuffle to prevent from a consistent pattern forming
    temp_pass_list = list(temp_pass)
    random.shuffle(temp_pass_list)

    #combine temp array to create password
    password = ''.join(temp_pass_list)

    print(f'\n{password}\n')

generate_pwd()