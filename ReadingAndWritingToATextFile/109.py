FILE_NAME = 'Subject.txt'


def main():
    selection = input('''
    1) Create a new file
    2) Display a file
    3) Add a new item to the file
    Make a selection 1, 2, 3: ''')

    if selection == '1':
        file = open(FILE_NAME, 'w')
        Subject = input('enter a subject ' )
        file.write(f'{Subject}\n')
        file.close
    elif selection == '2':
        file = open(FILE_NAME, 'r')
        print(file.read())
        file.close
    elif selection == '3':
        file = open(FILE_NAME, 'a')
        Subject = input('enter a new subject ' )
        file.write(f'{Subject}\n')
        file.close
        file = open(FILE_NAME, 'r')
        print(file.read())
        file.close
    else:
        print(f'{selection} is not a valid choice!!!!!!!')
    

   
main()        










































