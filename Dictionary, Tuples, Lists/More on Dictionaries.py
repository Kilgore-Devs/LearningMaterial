my_dictionary = {"key": "value", "new key": "new value"}
print(my_dictionary["new key"])
# values in dicts can me assigned to variables and used in expressions
val = my_dictionary["key"]
print(val)
print("I can print " + my_dictionary["new key"] + " from the dictionary!")
print("key" in my_dictionary)  # searches for the key in dict returns true if in
print("not a key" not in my_dictionary) # returns true if its not in
# dictionaries are unordered
print([2, 3, 4] == [2, 3, 4])
print([2, 3, 4] == [4, 3, 2])
# dictionary need to have same key:value pair to be considered equal.


