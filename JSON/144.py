import json
from tabulate import tabulate
import csv

data = json.load(open('bookinfo.json', encoding='utf8'))

def view(rows):
    print(tabulate(rows, headers="keys"))
          
def main():
    view(data["Authors"])
    Authors_name = input('Enter a Authors name. ')
    filtered_Authors = []

    for row in data["Authors"]:
        if row["Name"] == Authors_name:
            filtered_Authors.append(row)

    author_id = filtered_Authors[0]['ID']

    filtered_books = []
    for row in data["Books"]:
        if row["Author"] == author_id:
            filtered_books.append(row)
            row["Author"] = Authors_name
    
    view(filtered_books)
    fieldnames = filtered_books[0].keys()
    file_write = open("Books.csv", 'w', newline='') 
    csvwriter = csv.DictWriter(file_write, fieldnames=fieldnames)
    csvwriter.writeheader()
    csvwriter.writerows(filtered_books)
    file_write.close()
    

main()
          
          
          

