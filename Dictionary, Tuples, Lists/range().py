#  range() returns sequence of number usually used in for loop
something = range(10)  # one input
for num in something:
    print(num)  # prints 0-9

another = range(1, 6)  # two inputs
for num in another:
    print(num)  # prints 1-5

again = range(2, 20, 2)  # start at 2 and goes up to 18, by 2 or to go down (20, 0, 2)
for num in again:
    print(num)  # prints 2, 4 ,6...18