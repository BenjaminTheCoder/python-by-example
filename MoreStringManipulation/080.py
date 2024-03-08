def main():
    fname = input('enter your first name. ')
    lenfname = len(fname)
    print(f'your first name is {lenfname} letters.')
    lname = input('enter your last name. ')
    lenlname = len(lname)
    print(f'your last name is {lenlname} letters.')
    fullname = fname + ' ' + lname
    print(f'your full name is {fullname}.')
    lenfullname = len(fullname)
    print(f'your full name is {lenfullname} letters.')

main()
