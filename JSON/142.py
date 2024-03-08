import json
from tabulate import tabulate

data = json.load(open('bookinfo.json'))


def view(rows):
    print(tabulate(rows, headers="keys"))


#view(bookinfo["Authors"])
def get_name_by_ID(ID):
    for row in data["Authors"]:
        if row["ID"] == ID:
            return row["Name"]
    return None
    

##print(get_name_by_ID(1))
    

      
def main():
    view(data["Authors"])
    birth_place = input('Enter a birth place. ')
    filtered_birth_places = []
    for row in data["Authors"]:
        if row["Birthplace"] == birth_place:
            filtered_birth_places.append(row)

    author_ids = []
    for row in filtered_birth_places:
        author_ids.append(row['ID'])
    ##print('author_ids', author_ids)    

    
##    filtered_books = []
##    for row in data["Books"]:
##        if row["Author"] in author_ids:
##            filtered_books.append(row)
##    view(filtered_books)
##    
##    result_table = []

    filtered_books = []
    for row in data["Books"]:
        ##print('row', row)
        ##print('filtered_books before append', filtered_books)
        ##print('get_name_by_ID(row["Author"])', get_name_by_ID(row["Author"]))
        #get_name_by_ID(row["Author"])
        
        if row["Author"] in author_ids:
            ##print("inside if")
            filtered_books.append(row)
            row["Author"] = get_name_by_ID(row["Author"])
            ##print('filtered_books after append', filtered_books)
        ##print()
        
    view(filtered_books)

##    result_table = [
##        {"Title": "De Profundis", "Author": "Oscar Wilde", "Year": 1905},
##        {"Title": "Lyrebird", "Author": "Cecelia Ahern", "Year": 2017},
##        {"Title": "Perfect", "Author": "Cecelia Ahern", "Year": 2017},
##        {"Title": "The Marble Collector", "Author": "Cecelia Ahern", "Year": 2016},
##        {"Title": "The Pictrure of Dorian Gray", "Author": "Oscar Wilde", "Year": 1890},
##        {"Title": "The Year I Met You", "Author": "Cecelia Ahern", "Year": 2014},
##    ]   
    #view(result_table)
    




main()

