import csv


def main():
    file = open('Books.csv', 'r')
    reader = csv.reader(file)
    books = list(reader)
    #print('books', books, type(books))
    filteredbooks = []
    start = int(input('Enter the starting year.'))
    #print('start', start, type(start))
    end = int(input('Enter the ending year.'))
    #print('end', end, type(end))
    for book in books:        
        #print('book', book, type(book))
        year = int(book[2])
        #print('year', year, type(year))
        if year >= start and year <= end:
            filteredbooks.append(book)
        #print('filteredbooks', filteredbooks,type(filteredbooks))
        
        




    for book in filteredbooks:
        print(book)

        

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


##johnGreeter = greet('John')
##benGreeter = greet('Ben') 
##johnGreeter()
##benGreeter()
    

main2()        










































