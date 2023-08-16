# useful for when you want a collection of items and you don't want dupes and don't care about order
set1 = {1, 2, 3, 4, 5}
set2 = set({6, 7, 8, 9, 10})
# items in a set are unordered
print(set2)
print(set1)
set3 = set()  # creates set you can edit later

set4 = set(range(0, 22, 2))  # creates set starting at 0 going to and stopping before 22, by 2
print(set4)
# set can hold items of diff data types
# cannot access by index, must use for loop
for num in set4:
    print(num)
print(22 in set4)  # checks if 22 is in set
numbers = [1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 9, 10]
print(set(numbers))  # if you have dupes in list and want to display without dupes, pass list to set() fx as an arg
print((len(numbers)))  # shows number with dupes
print(list(set(numbers)))
print(len(list(set(numbers))))  # shows number of non duped/unique numbers

#
