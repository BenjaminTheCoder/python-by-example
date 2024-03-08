Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d = {"red": "#ff0000", "green": "#00ff00", "blue": "#0000ff"}
d
{'red': '#ff0000', 'green': '#00ff00', 'blue': '#0000ff'}
d["red"]
'#ff0000'
d = {"red": (255,0,0), "green": (0,255,0), "blue": (0,0,255)}
d
{'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
d["blue"]
(0, 0, 255)
d = {"red": (255,0,0), "green": (0,255,0), "blue": (0,0,255)}
d["yellow"]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d["yellow"]
KeyError: 'yellow'
d = {"Ben": {"first_name": "Ben", "last_name": "Alexander", "age": 9}}
d
{'Ben': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}}
d = {"Ben": {"first_name": "Ben", "last_name": "Alexander", "age": 9}, }
dd = {"Ben": {"first_name": "Ben", "last_name": "Alexander", "age": 9}, }d = {"Ben": {"first_name": "Ben", "last_name": "Alexander", "age": 9}, }d = {"Ben": {"first_name": "Ben", "last_name": "Alexander", "age": 9}}
SyntaxError: invalid syntax
d = {"Ben": {"first_name": "Ben", "last_name": "Alexander", "age": 9}, "Kima": {"first_name": "Kima", "last_name": "Alexander", "age": 9}}
d
{'Ben': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}, 'Kima': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9}}
from pprint import pprint
from tabulate import tabulate
pprint(d)
{'Ben': {'age': 9, 'first_name': 'Ben', 'last_name': 'Alexander'},
 'Kima': {'age': 9, 'first_name': 'Kima', 'last_name': 'Alexander'}}
tabulate(d)
'----------  ----------\nfirst_name  first_name\nlast_name   last_name\nage         age\n----------  ----------'
print(tabulate(d))
----------  ----------
first_name  first_name
last_name   last_name
age         age
----------  ----------
print(tabulate(d.value()))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(tabulate(d.value()))
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
print(tabulate(d.values()))
----  ---------  -
Ben   Alexander  9
Kima  Alexander  9
----  ---------  -




print(tabulate(d.values(), headers="keys"))
first_name    last_name      age
------------  -----------  -----
Ben           Alexander        9
Kima          Alexander        9
d
{'Ben': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}, 'Kima': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9}}
d["Oleg"] = {"first_name": "Oleg", "last_name": "Alexander", "age": 43}
d
{'Ben': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}, 'Kima': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9}, 'Oleg': {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 43}}
pprint(d)
{'Ben': {'age': 9, 'first_name': 'Ben', 'last_name': 'Alexander'},
 'Kima': {'age': 9, 'first_name': 'Kima', 'last_name': 'Alexander'},
 'Oleg': {'age': 43, 'first_name': 'Oleg', 'last_name': 'Alexander'}}
del(d["Oleg"])
d
{'Ben': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}, 'Kima': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9}}
d["Oleg"] = {"first_name": "Oleg", "last_name": "Alexander", "age": 43}
pprint(d)
{'Ben': {'age': 9, 'first_name': 'Ben', 'last_name': 'Alexander'},
 'Kima': {'age': 9, 'first_name': 'Kima', 'last_name': 'Alexander'},
 'Oleg': {'age': 43, 'first_name': 'Oleg', 'last_name': 'Alexander'}}
d["Oleg"]["age"] = 27
pprint(d)
{'Ben': {'age': 9, 'first_name': 'Ben', 'last_name': 'Alexander'},
 'Kima': {'age': 9, 'first_name': 'Kima', 'last_name': 'Alexander'},
 'Oleg': {'age': 27, 'first_name': 'Oleg', 'last_name': 'Alexander'}}
d.value()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
d.values()
dict_values([{'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}, {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9}, {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27}])
pprint(d.value())
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    pprint(d.value())
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
pprint(d.values())
dict_values([{'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}, {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9}, {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27}])
enumerate(d.values())
<enumerate object at 0x000001E61E452930>
list(enumerate(d.values()))
[(0, {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}), (1, {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9}), (2, {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27})]
dict(enumerate(d.values()))
{0: {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9}, 1: {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9}, 2: {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27}}
d = dict(enumerate(d.values()))
pprint(d)
{0: {'age': 9, 'first_name': 'Ben', 'last_name': 'Alexander'},
 1: {'age': 9, 'first_name': 'Kima', 'last_name': 'Alexander'},
 2: {'age': 27, 'first_name': 'Oleg', 'last_name': 'Alexander'}}
d[0]['id'] = '0'
d[1]['id'] = '1'
d[2]['id'] = '2'
pprint(d)
{0: {'age': 9, 'first_name': 'Ben', 'id': '0', 'last_name': 'Alexander'},
 1: {'age': 9, 'first_name': 'Kima', 'id': '1', 'last_name': 'Alexander'},
 2: {'age': 27, 'first_name': 'Oleg', 'id': '2', 'last_name': 'Alexander'}}
list((str(id, val) for id, val in enumerate(d.values()))
     
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
list([(str(id), val) for id, val in enumerate(d.values())])
     
[('0', {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9, 'id': '0'}), ('1', {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9, 'id': '1'}), ('2', {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27, 'id': '2'})]
d = dict([(str(id), val) for id, val in enumerate(d.values())])
     
pprint(d)
     
{'0': {'age': 9, 'first_name': 'Ben', 'id': '0', 'last_name': 'Alexander'},
 '1': {'age': 9, 'first_name': 'Kima', 'id': '1', 'last_name': 'Alexander'},
 '2': {'age': 27, 'first_name': 'Oleg', 'id': '2', 'last_name': 'Alexander'}}
import json
json.dump(d, open('json_test.json','w'), indent=4)
d1 = {
    "0": {
        "first_name": "Ben",
        "last_name": "Alexander",
        "age": 9,
        "id": "0"
    },
    "1": {
        "first_name": "Kima",
        "last_name": "Alexander",
        "age": 9,
        "id": "1"
    },
    "2": {
        "first_name": "Oleg",
        "last_name": "Alexander",
        "age": 27,
        "id": "2"
    }
}
d1
{'0': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9, 'id': '0'}, '1': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9, 'id': '1'}, '2': {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27, 'id': '2'}}
d
{'0': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9, 'id': '0'}, '1': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9, 'id': '1'}, '2': {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27, 'id': '2'}}
cubing_records = {'0': {'id': '0', 'person_id': '0', 'record': 29.0}}
cubing_records['1'] = {'id': '1', 'person_id': '3', 'record': 3.33}
d
{'0': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9, 'id': '0'}, '1': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9, 'id': '1'}, '2': {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27, 'id': '2'}}
people = d
people
{'0': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9, 'id': '0'}, '1': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9, 'id': '1'}, '2': {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27, 'id': '2'}}
people['3'] = {'id': '3', 'first_name': 'Max', 'last_name': 'Park', 'age': 30}
pprint(people)
{'0': {'age': 9, 'first_name': 'Ben', 'id': '0', 'last_name': 'Alexander'},
 '1': {'age': 9, 'first_name': 'Kima', 'id': '1', 'last_name': 'Alexander'},
 '2': {'age': 27, 'first_name': 'Oleg', 'id': '2', 'last_name': 'Alexander'},
 '3': {'age': 30, 'first_name': 'Max', 'id': '3', 'last_name': 'Park'}}
pprint(cubing_records)
{'0': {'id': '0', 'person_id': '0', 'record': 29.0},
 '1': {'id': '1', 'person_id': '3', 'record': 3.33}}
cubing_records['2'] = {'id': '2', 'person_id': '1', 'record': None}
pprint(cubing_records)
{'0': {'id': '0', 'person_id': '0', 'record': 29.0},
 '1': {'id': '1', 'person_id': '3', 'record': 3.33},
 '2': {'id': '2', 'person_id': '1', 'record': None}}
data = {'people': people, 'cubing_records': cubing_records}
pprint(data)
{'cubing_records': {'0': {'id': '0', 'person_id': '0', 'record': 29.0},
                    '1': {'id': '1', 'person_id': '3', 'record': 3.33},
                    '2': {'id': '2', 'person_id': '1', 'record': None}},
 'people': {'0': {'age': 9,
                  'first_name': 'Ben',
                  'id': '0',
                  'last_name': 'Alexander'},
            '1': {'age': 9,
                  'first_name': 'Kima',
                  'id': '1',
                  'last_name': 'Alexander'},
            '2': {'age': 27,
                  'first_name': 'Oleg',
                  'id': '2',
                  'last_name': 'Alexander'},
            '3': {'age': 30,
                  'first_name': 'Max',
                  'id': '3',
                  'last_name': 'Park'}}}
>>> json.dump(data, open('json_test.json','w'), indent=4)
>>> data_loaded = json.load(open('json_test.json'))
>>> pprint(data_loaded)
{'cubing_records': {'0': {'id': '0', 'person_id': '0', 'record': 29.0},
                    '1': {'id': '1', 'person_id': '3', 'record': 3.33},
                    '2': {'id': '2', 'person_id': '1', 'record': None}},
 'people': {'0': {'age': 9,
                  'first_name': 'Ben',
                  'id': '0',
                  'last_name': 'Alexander'},
            '1': {'age': 9,
                  'first_name': 'Kima',
                  'id': '1',
                  'last_name': 'Alexander'},
            '2': {'age': 27,
                  'first_name': 'Oleg',
                  'id': '2',
                  'last_name': 'Alexander'},
            '3': {'age': 30,
                  'first_name': 'Max',
                  'id': '3',
                  'last_name': 'Park'}}}
>>> data_loaded['people']
{'0': {'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9, 'id': '0'}, '1': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9, 'id': '1'}, '2': {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27, 'id': '2'}, '3': {'id': '3', 'first_name': 'Max', 'last_name': 'Park', 'age': 30}}
>>> data_loaded['people']['0']
{'first_name': 'Ben', 'last_name': 'Alexander', 'age': 9, 'id': '0'}
>>> data_loaded['people']['0']['first_name']
'Ben'
>>> data_loaded['people']['0']['first_name'] = 'Benjamin'
>>> data_loaded['people']
{'0': {'first_name': 'Benjamin', 'last_name': 'Alexander', 'age': 9, 'id': '0'}, '1': {'first_name': 'Kima', 'last_name': 'Alexander', 'age': 9, 'id': '1'}, '2': {'first_name': 'Oleg', 'last_name': 'Alexander', 'age': 27, 'id': '2'}, '3': {'id': '3', 'first_name': 'Max', 'last_name': 'Park', 'age': 30}}
