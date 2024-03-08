from functools import partial

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
len_alphabet = len(alphabet)

def shift_letter(sign, letter, shifting):
    index = alphabet.index(letter)
    new_index = index + (shifting * sign)
    num1 = len_alphabet - (shifting * sign)
    wrapping = index - num1
    if new_index >= len_alphabet:
        newletter = alphabet[wrapping]
    else:
        newletter = alphabet[new_index]

    return newletter

def make_code(deshift_or_shiftfunc):
    message = input('Enter a message!!!').lower()
    num_of_shifting = int(input('Enter a shift number!!!'))
    broken_message = list(message)
    letters = []
    for char in broken_message:
        newletter = deshift_or_shiftfunc(char, num_of_shifting)
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
            make_code(partial(shift_letter, 1))
        case '2':
            make_code(partial(shift_letter, -1))
        case '3':
            quit()
        case _:
            print("Invalid case!")
    main()  

main()
