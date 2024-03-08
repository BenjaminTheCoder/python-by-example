import csv


def main():
    file = open('Books.csv', 'w')
    Book1 = 'To Kill A Mocking Bird,Harper Lee,1960\n'
    Book2 = 'A Breif History of Time,Stephen Hawking,1988\n'
    Book3 = 'The Great Gatsby,F. Scott Fitzgerald,1922\n'
    Book4 = 'The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\n'
    Book5 = 'Pride and Prejudice,Jane Austen,1813\n'
    file.write(Book1)
    file.write(Book2)
    file.write(Book3)
    file.write(Book4)
    file.write(Book5)
    file.close()
    
def main2():
    dict_data = [{"book":"To Kill A Mocking Bird", "author": "Harper Lee", "year": "1960"},
            {"book":"A Breif History of Time", "author": "Stephen Hawking", "year": "1988"},
            {"book":"The Great Gatsby", "author": "F. Scott Fitzgerald", "year": "1922"},
            {"book":"The Man Who Mistook His Wife for a Hat", "author": "Oliver Sacks", "year": "1985"},
            {"book":"Pride and Prejudice", "author": "Jane Austen", "year": "1813"},
            ]


    csv_columns = ['book','author','year']

    csv_file = "Books2.csv"
    csvfile = open(csv_file, 'w')
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)
    csvfile.close()

    csvfile = open(csv_file, 'r')
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['book'])
    csvfile.close()

   
main2()        










































