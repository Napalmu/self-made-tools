import argparse
import pyfiglet
from random import choice, randint, shuffle
from enum import Enum

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
    parser.add_argument('-leet', '--leet_speak_obfuscation', type=bool, help="Obfuscate password with leetspeak")
    parser.add_argument('-obf', '--obfuscate', type=int, help="Obfuscate password with intensity levels from 1 (mild) -3 (extreme)")

    return parser

class Wordlist(Enum):
    FINNISH = ['kaikkisanat.txt']
    ENGLISH = ['1000-most-common-words.txt']
    MIXED = ['kaikkisanat.txt', '1000-most-common-words.txt']

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
    global password
    password = pw
    return pw

#Obfucate string using leetspeak for example with an intensity level
def obfuscate_string(string_to_obfuscate, level="moderate"):
    levels = {
        "mild": str.maketrans({"e": "3", "o": "0"}),
        "moderate": str.maketrans({"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}),
        "extreme": str.maketrans({"a": "4", "b": "8", "e": "3", "g": "9", "i": "1",
                                  "l": "1", "o": "0", "s": "5", "t": "7", "z": "2"})
    }
    # Apply the corresponding translation map
    obfuscated_string = string_to_obfuscate.translate(levels.get(level, levels[level]))
    #print(string_to_obfuscate)
    #print(obfuscated_string)
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

# Using wordlists, create a password by combining the lines found in said wordlists
def create_password_paragraph(language, number_of_words: int=3):
    pw = ""
    lines = []
    for wordlist in language:
        lines += open(wordlist).read().splitlines()
    shuffle(lines)
    for i in range(number_of_words):
        pw += choice(lines).capitalize()
    global password
    password = pw
    return pw

def main(): 
    parser = initialize_parser()
    args = vars(parser.parse_args())
    print(pyfiglet.figlet_format("PWGEN"))
    integer_value = args['length']
    #print(args)
    if args['default'] == True:
        print("Generated default password: " + create_password())
    if args['finnish_password_paragraph']:
        print("Generated finnish password paragraph: " + create_password_paragraph(Wordlist.FINNISH.value, args['finnish_password_paragraph']))
    if args['english_password_paragraph']:
        print("Generated english password paragraph: " + create_password_paragraph(Wordlist.ENGLISH.value, args['english_password_paragraph']))
    if args['mixed_password_paragraph']:
        print("Generated mixed password paragraph: " + create_password_paragraph(Wordlist.MIXED.value, args['mixed_password_paragraph']))
    if args['obfuscate']:
        print("Obfuscated pw: "+ obfuscate_string(password))
    if args['length']:        
        try:
            print("Generated password: " + create_password(integer_value))
            #length = input("How long should your password be?")
        except ValueError:
            print("\n Please enter a valid length!")
    
if __name__ == "__main__":
    main()