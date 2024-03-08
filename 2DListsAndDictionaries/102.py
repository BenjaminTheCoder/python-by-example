


def main():
    peeps = {}
    for i in range (4):
        name = input('enter a name. ')
        shoe = float(input('enter a shoe size. '))
        age = int(input('enter a age. '))
        peeps[name] = {'age': age, 'shoe size': shoe}
    row = input(f'enter one of the names. {list(peeps.keys())}. ')
    print(peeps[row])


main()        










































