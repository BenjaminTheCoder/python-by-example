import json
from tabulate import tabulate

def view(rows):
    print(tabulate(rows, headers="keys"))

authors = [
    {"ID": 1, "Name": "Agatha Christie", "Birthplace": "Torquay"},
    {"ID": 2, "Name": "Cecelia Ahern",   "Birthplace": "Dublin"},
    {"ID": 3, "Name": "J.K. Rowling",    "Birthplace": "Bristol"},
    {"ID": 4, "Name": "Oscar Wilde",     "Birthplace": "Dublin"},
]

books = [
    {"ID": 1,  "Title": "De Profundis",                             "Author": 4, "Year": 1905},
    {"ID": 2,  "Title": "Hary Potter And The Chamber Of Secrets",   "Author": 3, "Year": 1998},
    {"ID": 3,  "Title": "Hary Potter And The Prisoner Of Azkaban",  "Author": 3, "Year": 1999},
    {"ID": 4,  "Title": "Lyrebird",                                 "Author": 2, "Year": 2017},
    {"ID": 5,  "Title": "Murder On The Orient Express",             "Author": 1, "Year": 1934},
    {"ID": 6,  "Title": "Perfect",                                  "Author": 2, "Year": 2017},
    {"ID": 7,  "Title": "The Marble Collector",                     "Author": 2, "Year": 2016},
    {"ID": 8,  "Title": "The Murder On The Links",                  "Author": 1, "Year": 1923},
    {"ID": 9,  "Title": "The Pictrure of Dorian Gray",              "Author": 4, "Year": 1890},
    {"ID": 10, "Title": "The Secret Adversary",                     "Author": 1, "Year": 1921},
    {"ID": 11, "Title": "The Seven Dials Mystery",                  "Author": 1, "Year": 1929},
    {"ID": 12, "Title": "The Year I Met You",                       "Author": 2, "Year": 2014},
]

result_table = [
    {"Title": "De Profundis", "Author": "Oscar Wilde", "Year": 1905},
    {"Title": "Lyrebird", "Author": "Cecelia Ahern", "Year": 2017},
    {"Title": "Perfect", "Author": "Cecelia Ahern", "Year": 2017},
    {"Title": "The Marble Collector", "Author": "Cecelia Ahern", "Year": 2016},
    {"Title": "The Pictrure of Dorian Gray", "Author": "Oscar Wilde", "Year": 1890},
    {"Title": "The Year I Met You", "Author": "Cecelia Ahern", "Year": 2014},
]

bookinfo = {"Authors": authors, "Books": books}
json.dump(bookinfo, open('bookinfo.json', 'w'), indent=2)
view(bookinfo["Authors"])
print()
view(bookinfo["Books"])
