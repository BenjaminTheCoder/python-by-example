


def main():
    file = open('Names.txt', 'r')
    namesstr = file.read()
    file.close()
    print(namesstr)
    name = input(f'enter one of the names. ')
    nameslist = list(namesstr.split('\n'))
    index = nameslist.index(name) 
    del nameslist[index]
    file = open('Names2.txt', 'w')
    for name in nameslist:
        file.write(f'{name}\n')
    file.close()

def main2():
    file = open('Names.txt', 'r')
    namesstr = file.read()
    file.close()
    print(namesstr)
    name = input(f'enter one of the names. ')
    nameslist = list(namesstr.split('\n'))
    index = nameslist.index(name) 
    del nameslist[index]
    file = open('Names2.txt', 'w')
    file.write('\n'.join(nameslist))
    file.close()   
    

     

   
main()        










































