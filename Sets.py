# sets - used to store multiple items in a single variable.
# Sets are unordered, unchangeable (still can add and remove items) and unindexed.
# no dupes
burger_toppings = {"cheese", "lettuce", "bacon"}
print(burger_toppings)

pizza_toppings = {"cheese","pepperoni", "cheese", True, 1, 2, 3}  # dupes are ignored, True and 1 are same, so ignored.
print(pizza_toppings)

print(len(pizza_toppings))  # prints length, still ignores dupes
# demo of data types for sets..str, bool, int.
set_a = {"grape", "kiwi", "lemon"}
set_b = {1, 2, 3, 4, 5}
set_c = {False, True, False}
set_d = {"abc", 21, True, 54, "blue"}  # can have a mix of data type as values
# for python, sets are def as obj with datatype set.
set_f = {"USA", "Mexico", "Brazil"}
print(type(set_f))
# use set() constructor to create a set.
set_g = set(("Ford", "Chevy", "Honda")) # note the double round-brackets
print(set_g)
"""
Python Collections:
4 diff collection data types;
Lists = ordered and changeable. Allows dupes.
Tuple = ordered and unchangeable. Allows dupes.
Set = unordered, unchangeable, and unindexed. NO dupes. 
Dictionary = ordered, changeable. No dupes.
"""