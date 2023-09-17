#project :random password generator
'''
input :5
output: 12-jk
'''

import string
import random
letters=string.ascii_letters
number=string.digits
punctuation=string.punctuation
def password_generator(length):
    printable=f'{letters}{number}{punctuation}'
    printable=list(printable)
    random.shuffle(printable)
    random_password=random.choices(printable,k=length)
    random_password= ''.join(random_password)
    return(random_password)
def get_password_length():
    password_lenght=input("How long do you want your password :")
    return int(password_lenght)
def main():
    password_length=get_password_length()
    password=password_generator(password_length)
    
    print(password)


if __name__ =="__main__":
    main()
