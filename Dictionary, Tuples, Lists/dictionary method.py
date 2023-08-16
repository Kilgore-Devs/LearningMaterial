# Dicts are immutable like lists, variables that have been assigned dictionaries also hold refrences to dictionaries.
# Changes to vrialble will affect the dictionary
mycars = {"Ford": "Mustang", "Acura": "MDX", "BMW": "M3"}
print(mycars.keys())  # prints keys
print("Dodge" in mycars.values())  # returns false if not found
if "Dodge" in mycars:  # checks for key
    print(mycars["Dodge"])
else:
    print("Key not found.")

print(mycars.get("Dodge", "Using the get method, this key is not found"))

for key in mycars.keys():  # loops through and prints keys. "key" can be whatever ie key, k-as long as easy to define
    print(key)


for value in mycars.values():  # loops through and prints values
    print(value)


for items in mycars.items():  # iterates through and prints items
    print(items)  # will return list of tuples

for key, value in mycars.items():
    print(key, value)

print(len(mycars))  # shows number of key value pairs
# .popitem() removes last item in dict
mycars.pop("Ford")
print(mycars)

popped_variable = mycars.pop("Acura")
print(mycars)

print(len(mycars))  # shows number of key value pairs

newdict = {}.fromkeys(["fruit"], "orange")
print(newdict)

newdict = {}.fromkeys("fruit", "orange")  # each char in iterable used as key, repeated chars are ignore
print(newdict)
# dictname.clear() will remove everything in dict
# to create a copy with its own reference
copycars = mycars.copy()
print(copycars)

# whateveryouwanttoupdate.update(dict you want key value pairs assigned from)
online_courses = {"Udemy": "Python", "Youtube": "HTML", "Coursera": "CSS"}  # creates dic
additional = {"ZTM": "React"} # creates another dict
online_courses.update(additional)  # adds additional dict to online dict
all_courses = online_courses.copy()  # creates new dict with a copy of online dict
online_courses.clear()  # clears online dict
print(online_courses)  # prints online dict...its empty {}
print(all_courses)  # prints all courses dict
#set
if "Udemy Businness" not in all_courses:  # not true so it runs.. give key a value if not found
    all_courses["Udemy Business"] = "Rust"


print(all_courses)

all_courses.setdefault("YT.com", "WebDev") # check for key and assigns value. Doesnt overwrite pre-existing keys
print(all_courses)

# dict() creates a  dictionary

empty = dict()
print(empty)
notemppty = dict(a=1, b=2, c=3)  # cant use numbers as keys
print(notemppty)
