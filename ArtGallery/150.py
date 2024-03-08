import json
from tabulate import tabulate

FILENAME = "cube_repair_shop.json"

data = json.load(open(FILENAME, encoding='utf8'))

def view(rows):
    print(tabulate(rows, headers="keys"))

def save():
    json.dump(data, open(FILENAME, 'w', encoding='utf8'), indent=2)

def search_by_name():
    name = input('Enter a name.').lower()
    
    customerIds = []
    for cust in data['customers']:
        if name in cust['name'].lower():            
            customerIds.append(cust['id'])
            
    customerIdsInWork = []
    for wcust in data['work_orders']:
        if wcust['customer_id'] in customerIds:            
            customerIdsInWork.append(wcust)
    if len(customerIdsInWork) == 0:
        print('No work orders found :(')
    else:
        view(customerIdsInWork)

def add_customer():
    IDs = []
    for row in data['customers']:
        IDs.append(row['id'])

    new_ID = max(IDs)+1

    Name = input('Enter a name.')
    phoneNumber = input('Enter a phone number.')
    newPerson = {'id': new_ID, 'name': Name, 'phone': phoneNumber}
    data['customers'].append(newPerson)

    save()
    view(data['customers'])

def add_cube():
    IDs = []
    for row in data['cubes']:
        IDs.append(row['id'])
        
    new_ID = max(IDs)+1

    name = input('Enter a name.')
    brand = input('Enter a brand.')
    type_ = input('Enter a type')
    new_cube = {'id': new_ID, 'name': name,'brand': brand, 'type': type_}
    data['cubes'].append(new_cube)

    save()
    view(data['cubes'])

def add_work_order():
    
    IDs = []
    for row in data['work_orders']:
        IDs.append(row['id'])
        
    new_ID = max(IDs)+1
    view(data['customers'])
    customer_id = int(input('Enter a customer id.'))
    customer_ids = []
    for cust in data['customers']:
        customer_ids.append(cust['id'])        
        
    if customer_id not in customer_ids:
        print('Invalid customer id try again.')
        return
    view(data['cubes'])
    cube_id = int(input('Enter a cube id.'))
    cube_ids = []
    for cube in data['cubes']:
        cube_ids.append(cube['id'])
        
    if cube_id not in cube_ids:
        print('Invalid cube id try again.')
        return
    what_is_wrong = input('Enter what is wrong.')
    estimated_price = float(input('Enter the estimated price.'))
    new_work_order = {'id': new_ID, 'customer_id': customer_id, 'cube_id': cube_id, 'what_is_wrong': what_is_wrong, 'estimated_price': estimated_price,}
    data['work_orders'].append(new_work_order)

    save()
    view(data['work_orders'])

def main():
    while True:
        print('')
        print("Ben's Cube Repair")
        print('')
        asking = int(input(''' Hi this is "Ben's Cube Repair"
         your hired
         here is the main files and what you can do with them.
        1) Add a customer
        2) Add a cube
        3) Add a work order
        4) View customer file
        5) View cube file
        6) View work order file
        7) Search work orders by customer ID
        8) Save Files and Go on Break
            Use the numbers and descriptions above to get around the place
        '''))

        match asking:
            case 1:
                add_customer()
            case 2:
                add_cube()
            case 3:
                add_work_order()
            case 4:
                view(data["customers"])
            case 5:
                view(data["cubes"])
            case 6:
                view(data["work_orders"])
            case 7:
                search_by_name()
            case 8:
                save()
                break
            case _:
                print("Invalid case!")
                
    print('Bye')
    

main()
































# {
#   "Authors": [
#     {
#       "ID": 1,
#       "Name": "Agatha Christie",
#       "Birthplace": "Torquay"
#     },
#     {
#       "ID": 2,
#       "Name": "Cecelia Ahern",
#       "Birthplace": "Dublin"
#     },
#     {
#       "ID": 3,
#       "Name": "J.K. Rowling",
#       "Birthplace": "Bristol"
#     },
#     {
#       "ID": 4,
#       "Name": "Oscar Wilde",
#       "Birthplace": "Dublin"
#     }
#   ],
#   "Books": [
#     {
#       "ID": 1,
#       "Title": "De Profundis",
#       "Author": 4,
#       "Year": 1905
#     },
#     {
#       "ID": 2,
#       "Title": "Hary Potter And The Chamber Of Secrets",
#       "Author": 3,
#       "Year": 1998
#     },
#     {
#       "ID": 3,
#       "Title": "Hary Potter And The Prisoner Of Azkaban",
#       "Author": 3,
#       "Year": 1999
#     },
#     {
#       "ID": 4,
#       "Title": "Lyrebird",
#       "Author": 2,
#       "Year": 2017
#     },
#     {
#       "ID": 5,
#       "Title": "Murder On The Orient Express",
#       "Author": 1,
#       "Year": 1934
#     },
#     {
#       "ID": 6,
#       "Title": "Perfect",
#       "Author": 2,
#       "Year": 2017
#     },
#     {
#       "ID": 7,
#       "Title": "The Marble Collector",
#       "Author": 2,
#       "Year": 2016
#     },
#     {
#       "ID": 8,
#       "Title": "The Murder On The Links",
#       "Author": 1,
#       "Year": 1923
#     },
#     {
#       "ID": 9,
#       "Title": "The Pictrure of Dorian Gray",
#       "Author": 4,
#       "Year": 1890
#     },
#     {
#       "ID": 10,
#       "Title": "The Secret Adversary",
#       "Author": 1,
#       "Year": 1921
#     },
#     {
#       "ID": 11,
#       "Title": "The Seven Dials Mystery",
#       "Author": 1,
#       "Year": 1929
#     },
#     {
#       "ID": 12,
#       "Title": "The Year I Met You",
#       "Author": 2,
#       "Year": 2014
#     }
#   ]
# }
