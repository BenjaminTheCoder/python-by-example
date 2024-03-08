import csv


def main():
    file = open('Books.csv', 'a')
    book6t = input('Enter a book title. ')
    book6a = input('Enter a author. ')
    book6y = input('Enter a year. ')
    book6 = f'{book6t},{book6a},{book6y}'
    file.write(book6)
    file.close()
    file = open('Books.csv', 'r')
    print(file.read())
    file.close()
    
    
    
    
##def main2():
##    dict_data = [{"book":"To Kill A Mocking Bird", "author": "Harper Lee", "year": "1960"},
##            {"book":"A Breif History of Time", "author": "Stephen Hawking", "year": "1988"},
##            {"book":"The Great Gatsby", "author": "F. Scott Fitzgerald", "year": "1922"},
##            {"book":"The Man Who Mistook His Wife for a Hat", "author": "Oliver Sacks", "year": "1985"},
##            {"book":"Pride and Prejudice", "author": "Jane Austen", "year": "1813"},
##            ]
##
##
##    csv_columns = ['book','author','year']
##
##    csv_file = "Books2.csv"
##    csvfile = open(csv_file, 'w')
##    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
##    writer.writeheader()
##    for data in dict_data:
##        writer.writerow(data)
##    csvfile.close()
##
##    csvfile = open(csv_file, 'r')
##    reader = csv.DictReader(csvfile)
##    for row in reader:
##        print(row['book'])
##    csvfile.close()
##
   
main()        










































