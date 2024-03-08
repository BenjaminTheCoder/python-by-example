

def main():
    file = open('Names.txt', 'a')
    name = input('enter a name ' )
    file.write(f'{name}\n')
    
    file.close()


    
main()        










































