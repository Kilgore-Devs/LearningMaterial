# JSON is syntax for storing and exchanging data
# It is written with JavaScript obj notation.
import json
x = '{ "name":"Jared", "age":30, "City":"Tampa Bay"}'  # some json
y = json.loads(x)  # convert json to python
print(y["City"])

# a dictionary (an object) in python and covert to json
z = {       # This is the object which happens to be a dictionary
  "name": "Glenn",
  "age": 51,
  "city": "New Jersey"
}

a = json.dumps(z)
print(a)
""" You're able to convert python object of these types into JSON strings:
dict, list, tuple, string, int, float, True, False, None"""

print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print(json.dumps({"alias": "Jack", "years": 58}))
print(json.dumps(["cherry", "orange"]))
print(json.dumps(("cherry", "orange")))
print(json.dumps("Howdy"))
""""
These are the conversions between Python and JSON
Python	JSON
dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null    
"""
h = {  # convert the object h that contains multiple legal data types
  "alias": "Ben",
  "gender": "male",
  "married": False,
  "divorced": True,
  "kids": ("Jeremy", "Madison"),
  "pets": True,
  "cars": [
    {"model": "Dodge Viper", "mpg": 12.5},
    {"model": "Harley Davidson", "mpg": 22}
  ]
}

print(json.dumps(h))  # prints json string

print(json.dumps(h, indent=3))  # formats with indentation to make it easier to read

print(json.dumps(h, separators=(" | ", " is ")))  # changes the default separators ,
print(json.dumps(h, sort_keys=True))  # changes separator and sorts it
