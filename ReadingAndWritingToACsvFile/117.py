import csv

FILENAME = "Books.csv"

def main():
    file = open(FILENAME, 'r')
    books = list(csv.reader(file))
    for i in range(len(books)):
        #print(f'{i} {books[i]}')
        year = books[i][2]
        author = books[i][1]
        print(f'© {year} {author}. All rights reserved.')
 

    
    
    
    
        




    

        

def apply_types_to_dict(fieldname_to_type_mapping, target_dict):
    return {k: fieldname_to_type_mapping[k](v) for k, v in target_dict.items()}

    
def main2():
    books = list(csv.DictReader(open('Books.csv'), fieldnames=['title', 'author', 'year']))
    books = list(map(lambda book: apply_types_to_dict({'title': str, 'author': str, 'year': int}, book), books))
    start = int(input('Enter the starting year.'))
    end = int(input('Enter the ending year.'))
    filteredbooks = list(filter(lambda book: book['year'] >= start and book['year'] <= end, books))

    for book in filteredbooks:
        print(book)    
    

# Closure
def greet(name):
 
    def innerFunction():
        print(f'Hi, {name}!')
 
    # Note we are returning function
    # WITHOUT parenthesis
    return innerFunction 


johnGreeter = greet('John')
benGreeter = greet('Ben') 
#johnGreeter()
#benGreeter()
    

main()        










































