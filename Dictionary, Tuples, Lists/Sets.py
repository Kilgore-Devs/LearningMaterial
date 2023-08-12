# sets - used to store multiple items in a single variable.
# Sets are unordered, unchangeable (still can add and remove items) and un-indexed.
# no dupes.
burger_toppings = {"cheese", "lettuce", "bacon"}
print(burger_toppings)

pizza_toppings = {"cheese", "pepperoni", "cheese", True, 1, 2, 3}  # dupes are ignored, True and 1 are same, so ignored.
print(pizza_toppings)

print(len(pizza_toppings))  # prints length, still ignores dupes.
# demo of data types for sets..str, bool, int.
set_a = {"grape", "kiwi", "lemon"}
set_b = {1, 2, 3, 4, 5}
set_c = {False, True, False}
set_d = {"abc", 21, True, 54, "blue"}  # can have a mix of data type as values.
# for python, sets are def as obj with datatype set.
set_f = {"USA", "Mexico", "Brazil"}
print(type(set_f))
# use set() constructor to create a set.
set_g = set(("Ford", "Chevy", "Honda"))  # note the double round-brackets.
print(set_g)
# cannot access items in a set by referring to index or key, must loop or see if specific value is present.
for z in set_g:  # loops through and prints set_g.
    print(z)
print("Pontiac" in set_g)  # check to see if pontiac is present, it's not and returns false.
set_g.add("Pontiac")  # adds Pontiac
print(set_g)
set_h = {"Lincoln", "Dodge", "Audi"}  # new set h.
set_g.update(set_h)  # updates/appends set_g with set_h.
print(set_g)
set_i = ["Mazda"]  # can update with any iterable object ie lists, tuples etc.
set_g.update(set_i)
print(set_g)
set_g.remove("Pontiac")
print(set_g)
# pop() removes random.
# clear() empties the set set.clear().
# del delete the set completely  del setname.

set_j = set_g.union(set_h)  # adds set h to set g. creates set j.
print(set_j)
set_g.update(set_h)  # inserts items in set_h into set_g.
print(set_g)

# How to keep or exclude duplicates
x = {"mustang", "thoroughbred", "stallion"}
y = {"mustang", "M3", "A4"}
x.symmetric_difference_update(y)  # returns a list and excludes the dupe mustang.
print(x)

m = {"mustang", "thoroughbred", "stallion"}
n = {"mustang", "M3", "A4"}
o = m.symmetric_difference(n)  # returns a set of all but dupe mustang.
print(o)

p = {"mustang", "thoroughbred", "stallion"}
q = {"mustang", "M3", "A4"}
p.intersection_update(q)  # will keep only the dupe--mustang.
print(p)

s = {"mustang", "thoroughbred", "stallion"}
t = {"mustang", "M3", "A4"}
u = s.intersection(t)  # returns a new set that only includes the dupe.
print(u)
# remember 1 and True are the same in sets and treated as dupes.

"""
Python Collections:
4 diff collection data types;
Lists = ordered and changeable. Allows dupes.
Tuple = ordered and unchangeable. Allows dupes.
Set = unordered, unchangeable, and un-indexed. NO dupes. 
Dictionary = ordered, changeable. No dupes.

Set Methods per w3
    Method	                                        Description
add()	                            Adds an element to the set
clear()	                            Removes all the elements from the set
copy()	                            Returns a copy of the set
difference()	                    Returns a set containing the difference between two or more sets
difference_update()     	        Removes the items in this set that are also included in another, specified set
discard()	                        Remove the specified item
intersection()	                    Returns a set, that is the intersection of two other sets
intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                    Returns whether two sets have a intersection or not
issubset()	                        Returns whether another set contains this set or not
issuperset()	                    Returns whether this set contains another set or not
pop()	                            Removes an element from the set
remove()	                        Removes the specified element
symmetric_difference()	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	    inserts the symmetric differences from this set and another
union()	                            Return a set containing the union of sets
update()	                        Update the set with the union of this set and others
"""
