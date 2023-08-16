# are immutable = cannot be changed.
# useful for data that will not be changed later in program.
# less space used in memory
tuple_1 = ("a", "b", "c")
tuple_2 = (2.1, False, [1, 2, 3])
tuple_3 = (1, 0, 1, 0)
tuple_4 = tuple("abcdefg")
print(tuple_4)
# access by index and slice
print(tuple_4[1])  # index 1
print(tuple_4[1:4])  # slice at index 1-3 or b, c, d
print(tuple_4.__sizeof__())  # shows size in bytes
# tuples can be used as keys in a dictionary

# can iterate or loop through
cities = ("Cincinnati", "Charleston", "Chicago")
for city in cities:
    print(city)

count = 0    # increment to iterate through index numbers in tuple
while count < len(cities):
    print(cities[count])
    count += 1

backwards = len(cities) - 1
while backwards >= 0:
    print(cities[backwards])
    backwards -= 1
# step is like slice but has 2 :s

numbers = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print(numbers[::2])  # stride length of 2
print(numbers[1::2])  # starts at index 1 and goes by 2
print(numbers[6::-1])  # starts at index 6 and goes left by 1
print(numbers[9::-2])  # starts at index 9 and goes right by 2
# nested tuples
nested = (("a", "b", "c"), (1, 2, 3), ("A", "B", "C"))
# acces vals form
print(nested[2]) # acceses 2 tuple in the tuple
print(nested[0][1])
newtup = (1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5)
print(newtup.count(1))  # counts how many times 1 appears in tuple
print(newtup.index(3))