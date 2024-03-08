import json
from tabulate import tabulate

data = json.load(open('bookinfo.json'))


def view(rows):
    print(tabulate(rows, headers="keys"))
    
def main():
    view(data["Books"])
    year = int(input('Enter a year. '))
    filtered_years = []
    #print('year', year)
    for row in data["Books"]:
        if row["Year"] > year:
            filtered_years.append(row)
    print(filtered_years)

    view(sorted(filtered_years, key=lambda row: row['Year']))

main()
