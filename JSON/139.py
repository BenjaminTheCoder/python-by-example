import json

data = {
    "Names": [
        {
            "ID": 1,
            "First Name": "Simon",
            "Surname": "Howels",
            "Phone Number": "01223 349752"
        },
        {
            "ID": 2,
            "First Name": "Karen",
            "Surname": "Phillips",
            "Phone Number": "0954 295773"
        },
        {   "ID": 3,
            "First Name": "Darren",
            "Surname": "Smith",
            "Phone Number": "01583 749012"
        },
        {   "ID": 4,
            "First Name": "Anne",
            "Surname": "Jones",
            "Phone Number": "01323 567322"
        },
        {   "ID": 5,
            "First Name": "Mark",
            "Surname": "Smith",
            "Phone Number": "01223 855534"
        }

    ]
}


##data = {'Names':[]}
##data['Names'].append({"ID": 1, "First Name": "Simon", "Surname": "Howels", "Phone Number": "01223 349752"})
##data['Names'].append({"ID": 2, "First Name": "Karen", "Surname": "Phillips", "Phone Number": "0954 295773"})


json.dump(data, open('phonebook.json', 'w'), indent=4)

