import csv


def main():
    file = open('Books.csv', 'r')
    author = input('enter a author. ' )
    reader = csv.reader(file)
    authorfound = False
    for row in reader:
        if author in str(row):
            authorfound = True
            print(row)

    if not authorfound:
        print('Author not in my data!')

    
    
    
    
    

main()        










































