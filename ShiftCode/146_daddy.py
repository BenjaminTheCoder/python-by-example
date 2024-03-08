alphabet = 'abcdefghijklmnopqrstuvwxyz '

def shift_letter(letter, shifting):
    return alphabet[(alphabet.index(letter) + shifting) % len(alphabet)]

def make_code(sign):
    message = input('Enter a message!!!').lower()
    num_of_shifting = int(input('Enter a shift number!!!'))
    return "".join([shift_letter(char, (num_of_shifting * sign)) for char in message])

def main():
    num = input('''
1) Make a code
2) Decode a message
3) Quit
Enter your choice:
''')
    match num:
        case '1':
            print(make_code(1))
        case '2':
            print(make_code(-1))
        case '3':
            quit()
        case _:
            print("Invalid case!")
    main()
    
main()