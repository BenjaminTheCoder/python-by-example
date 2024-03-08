Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> "This is a string."
'This is a string.'
>>> 'This is a string.'
'This is a string.'
>>> "I don't understand."
"I don't understand."
>>> "Hello\nBen"
'Hello\nBen'
>>> print("Hello\nBen")
Hello
Ben
>>> print("Hello\tBen")
Hello	Ben
>>> print("Hello \"Ben\"")
Hello "Ben"
>>> print('Hello \'Ben\'')
Hello 'Ben'
>>> print('Hello \ Ben')
Hello \ Ben
>>> print('Hello \\ Ben')
Hello \ Ben
>>> "C:\Users\olega\Documents\PythonByExample\Strings\020.py"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> r"C:\Users\olega\Documents\PythonByExample\Strings\020.py"
'C:\\Users\\olega\\Documents\\PythonByExample\\Strings\\020.py'
>>> name = "Ben"
>>> age = 8
>>> f"My name is {name} and I'm {age} years old"
"My name is Ben and I'm 8 years old"
>>> "My name is " + name + " and I'm " + age + " years old"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    "My name is " + name + " and I'm " + age + " years old"
TypeError: must be str, not int
>>> "My name is " + name + " and I'm " + str(age) + " years old"
"My name is Ben and I'm 8 years old"
>>> "My name is %s and I'm %s years old" % (name, age)
"My name is Ben and I'm 8 years old"
>>> "My name is %s and I'm %s years old" % (name)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    "My name is %s and I'm %s years old" % (name)
TypeError: not enough arguments for format string
>>> "My name is %s and I'm %s years old" % (name, age, age)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    "My name is %s and I'm %s years old" % (name, age, age)
TypeError: not all arguments converted during string formatting
>>> "My name is %s and I'm %s years old" % (name, age)
"My name is Ben and I'm 8 years old"
>>> "My name is %s and I'm years old" % name
"My name is Ben and I'm years old"
>>> """In here you can put anything
of any length and you can
even have "quotes" or 'single quotes' inside"""
'In here you can put anything\nof any length and you can\neven have "quotes" or \'single quotes\' inside'
>>> print("""In here you can put anything
of any length and you can
even have "quotes" or 'single quotes' inside""")
In here you can put anything
of any length and you can
even have "quotes" or 'single quotes' inside
>>> print(f"""In here you can put anything
of any length and you can
even have "quotes" or {name} inside""")
In here you can put anything
of any length and you can
even have "quotes" or Ben inside
>>> len(name)
3
>>> len("Kima")
4
>>> print(name.capitalize())
Ben
>>> lowerCaseName = "ben"
>>> lowerCaseName.capitalize()
'Ben'
>>> print("My name is " + name)
My name is Ben
>>> print("My name is " + name + " I'm " + str(age) + " year old")
My name is Ben I'm 8 year old
>>> print("My name is " + " year old")
My name is  year old
>>> lowerCaseName.upper()
'BEN'
>>> name.lower()
'ben'
>>> lowerCaseName.upper().lower()
'ben'
>>> sentence = "the python who coded a novel"
>>> sentence.title()
'The Python Who Coded A Novel'
>>> sentence = "    the python who coded a novel  "
>>> sentence.strip()
'the python who coded a novel'
>>> sentence.replace("python","gorilla")
'    the gorilla who coded a novel  '
>>> sentence.strip().replace("python","gorilla").title()
'The Gorilla Who Coded A Novel'
>>> title = sentence.strip().replace("python","gorilla").title()
>>> title
'The Gorilla Who Coded A Novel'
>>> list(title)
['T', 'h', 'e', ' ', 'G', 'o', 'r', 'i', 'l', 'l', 'a', ' ', 'W', 'h', 'o', ' ', 'C', 'o', 'd', 'e', 'd', ' ', 'A', ' ', 'N', 'o', 'v', 'e', 'l']
>>> title[0]
'T'
>>> title[2]
'e'
>>> title[-1]
'l'
>>> title[:4]
'The '
>>> title[4:]
'Gorilla Who Coded A Novel'
>>> title[4:10]
'Gorill'
>>> title[4:11]
'Gorilla'
>>> "a" in ["a","e","i","o","u"]
True
>>> "b" in ["a","e","i","o","u"]
False
>>> 
