''' 
The purpose of this program is to generate a password that depends on the inputs of the user which are
password_length, security_level (1, 2, 3, 4). In the end, a password with the chosen characteristics will
be printed to the terminal. Future additions to this program are planned which revolve around the user entering a 
password and the program printing information about the password which include the length and the security level 
by the defined requirments in the current program.
'''

from random import choice
from string import ascii_lowercase, ascii_letters, digits, punctuation
def password_generator():

    print('')
    print('Welcome to the Password Generator!')
    print('Please provide the necessary information to generate your desired password.')
    print('------------------------------------------------------------------------------------------------')

    while True:
        try:
            password_length = int(input('Enter the character length of your desired password: '))
            if password_length <= 0:
                print('Error: Password length must be a positive integer.')
                continue
            break
        except ValueError:
            print('Error: Password length must be an integer.')

    if input('Would you like to learn about the different security levels available for your password? (Y or N): ').upper() == 'Y':
        print('''
              There are  4 security levels available for your password:

              1. Very Low - This level only includes lowercase letters in the English Alphabet.
              2. Low - This level includes a combination of lowercase and uppercase letters in the English Alphabet.
              3. Medium - This level includes a combination of the contents of the Low Security Level and also numerical characters.
              4. High - This level includes a combination of the contents of the Medium Security Level and also all these special characters:  
              !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
              ''')

    while True:
        try:
            security_level = int(input('Enter the security level of your desired password (1-4): '))
            if security_level < 1 or security_level > 4:
                print('Error: Security level must be a number between 1 and 4.')
                continue
            break
        except ValueError:
            print('Error: Security level must be an integer.')

    if security_level == 1:
        characters = ascii_lowercase
    elif security_level == 2:
        characters = ascii_letters
    elif security_level == 3:
        characters = ascii_letters + digits
    elif security_level == 4:
        characters = ascii_letters + digits + punctuation

    password = ''.join(choice(characters) for _ in range(password_length))
    print(f'Your {password_length} character password with Level {security_level} Security is:\n{password}')


password_generator()
print('')
print('Thank you for using this program!')
if input('Would you like to use this program again? (Y or N): ').upper() == 'Y':
    print('')
    password_generator()
else:
    print('Goodbye!')
    print('------------------------------------------------------------------------------------------------')
