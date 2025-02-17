import argparse
import pyfiglet
from random import choice, randint

def initialize_parser():
    parser = argparse.ArgumentParser(
        prog="Password Generator",
        description="Password Generator on steroids",
        epilog="Made by Joonatan Merenluoto"
        )
    parser.add_argument('-d', '--default',
                        action='store_false'
                        )
    parser.add_argument('-l', '--length',
                        type=int,
                        help='Specify password length')
    parser.add_argument('-n', '--numbers', 
    type=int, help='Specify how many numbers')
    return parser


def create_password_base():
    base_numbers = "123456789"
    base_lowercase = "abcdefghijklmnopqrstuvwxyz"
    base_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_nordic_characters = "åäö"
    base_special_characters = "!@£#¤$%&/(){}=-" #incomplete
    return base_lowercase+base_uppercase+base_numbers
    
def create_password(length: int=12, password_paragraph: bool=False):
    base = create_password_base()
    x = 0
    pw = ""
    while x <= int(length)-1:
        pw += choice(base)
        x += 1
    return pw

def create_password_with_string(input_string):
    base = create_password_base()
    x = 0
    pw = ""
    while x <= int(length)-1-len(input_string):
        pw += choice(base)
        x += 1
    N = randint(0, len(input_string))
    pw = pw[:N]+ str(input_string) + pw[N:]
    return pw


def main(): 
    parser = initialize_parser()
    args = vars(parser.parse_args())
    print(pyfiglet.figlet_format("PWGEN"))
    integer_value = args['length']
    #print(args)
    if args['default']:
        print("Generated password: " + create_password())
    if args['length']:        
        try:
            print("Generated password: " + create_password(integer_value))
            #length = input("How long should your password be?")
        except ValueError:
            print("\n Please enter a valid length!")
        
   
    
if __name__ == "__main__":
    main()