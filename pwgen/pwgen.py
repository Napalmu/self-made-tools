import argparse
import pyfiglet
from random import choice, randint, shuffle

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
    parser.add_argument('-fp', '--finnish_password_paragraph', 
                        type=int, 
                        help='Specify how many words your finnish password paragraph should have')
    parser.add_argument('-ep', '--english_password_paragraph', 
                        type=int, 
                        help='Specify how many words your english password paragraph should have')
    parser.add_argument('-mp', '--mixed_password_paragraph', 
                        type=int, 
                        help='Specify how many words your english and finnish mixed password paragraph should have')

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

#WIP
def obfuscate_string(string_to_obfuscate):
    obfuscated_string = string_to_obfuscate
    return obfuscated_string

# Combine with obfuscate_string
def create_password_with_string(length: int=12, input_string: str=""):
    base = create_password_base()
    x = 0
    pw = ""
    while x <= int(length)-1-len(input_string):
        pw += choice(base)
        x += 1
    N = randint(0, len(input_string))
    pw = pw[:N]+ str(input_string) + pw[N:]
    return pw


#Refactor paragraph functionality into one function
def create_finnish_password_paragraph(number_of_words: int=3):
    pw = ""
    lines = open('kaikkisanat.txt').read().splitlines()
    for i in range(number_of_words):
        pw += choice(lines).capitalize()
    return pw

def create_english_password_paragraph(number_of_words: int=3):
    pw = ""
    lines = open('1000-most-common-words.txt').read().splitlines()
    for i in range(number_of_words):
        pw += choice(lines).capitalize()
    return pw

def create_mixed_password_paragraph(number_of_words: int=3):
    pw = ""
    lines = open('1000-most-common-words.txt').read().splitlines()
    lines += open('kaikkisanat.txt').read().splitlines()
    shuffle(lines)
    for i in range(number_of_words):
        pw += choice(lines).capitalize()
    return pw

def main(): 
    parser = initialize_parser()
    args = vars(parser.parse_args())
    print(pyfiglet.figlet_format("PWGEN"))
    integer_value = args['length']
    #print(args)
    if args['default']:
        print("Generated default password: " + create_password())
    if args['finnish_password_paragraph']:
        print("Generated finnish password paragraph: " + create_finnish_password_paragraph(args['finnish_password_paragraph']))
    if args['english_password_paragraph']:
        print("Generated english password paragraph: " + create_english_password_paragraph(args['english_password_paragraph']))
    if args['mixed_password_paragraph']:
        print("Generated mixed password paragraph: " + create_mixed_password_paragraph(args['mixed_password_paragraph']))
    if args['length']:        
        try:
            print("Generated password: " + create_password(integer_value))
            #length = input("How long should your password be?")
        except ValueError:
            print("\n Please enter a valid length!")
    
if __name__ == "__main__":
    main()