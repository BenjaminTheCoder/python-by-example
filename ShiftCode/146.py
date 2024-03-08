import json
from pprint import pprint
from tabulate import tabulate
from operator import itemgetter

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
len_alphabet = len(alphabet)

def shift_letter(letter, shifting):
    index = alphabet.index(letter)
    new_index = index + shifting
    num1 = len_alphabet - shifting
    wrapping = index - num1
    if new_index >= len_alphabet:
        newletter = alphabet[wrapping]
    else:
        newletter = alphabet[new_index]

    return newletter

    
def make_code():
    message = input('Enter a message!!!').lower()
    num_of_shifting = int(input('Enter a shift number!!!'))
    broken_message = list(message)
#     print(type(num_of_shifting))
    letters = []
    for char in broken_message:
        newletter = shift_letter(char, num_of_shifting)
        letters.append(newletter)
        
        
    word = "".join(letters)
    print(word)

    
#     for char in broken_message:
#         index = alphabet.index(char)
#         indexes = []
#         index.append(indexes)
        
        
def deshift_letter(letter, shifting):
    index = alphabet.index(letter)
    new_index = index - shifting
    unwrapping = index + new_index
    if new_index >= len_alphabet:
         newletter = alphabet[unwrapping]
    else:
        newletter = alphabet[new_index]

    return newletter
    
    
def decode_message():
    message = input('Enter a  encoded message. ').lower()
    num_of_shifting = int(input("Enter it's shift number."))
    broken_message = list(message)
#     print(type(num_of_shifting))
    letters = []
    for char in broken_message:
        newletter = deshift_letter(char, num_of_shifting)
        letters.append(newletter)
    word = "".join(letters)
    print(word)
    
    
    
def main():
    num = input('''
1) Make a code
2) Decode a message
3) Quit
Enter your choice:
''')

    match num:
        case '1':
            make_code()
        case '2':
            decode_message()
        case '3':
            quit()
        case _:
            print("Invalid case!")
    main()
    

main()
