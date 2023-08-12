""" An iterator is an object that contains a countable number of values.
It's an object that can be iterated on. AKA can travers through all the values.
iterator is an object which implements the iterator protocol
__iter__() and __next__()

Dictionaries, tuples, and lists are iterable object aka iterable containers,
which can get an iterator from.
All the objects have an iter() method which is used to get an iterator."""
this_tuple = ("orange", "cherry", "kiwi")  # creates tuple
this_iter = iter(this_tuple)  # add iter to iterate through each item in tuple

print(next(this_iter))  # prints first iteration
print(next(this_iter))  # prints second iteration
print(next(this_iter))  # prints third iteration

# Strings are also iterable objects and can return an iterator.
this_string = "apple"
new_iter = iter(this_string)

print(next(new_iter))  # Starts iteration through apple, prints first letter.
print(next(new_iter))  # Iterates to and prints second letter.
print(next(new_iter))  # Iterates to and prints third letter.
print(next(new_iter))  # Iterates to and prints fourth letter.
print(next(new_iter))  # Iterates to and prints fifth letter.
# print(next(new_iter)) Will error due to no more letters in apple.

# Can also use a for loop to iterate through an iterable object.
# the for loop creates an iterator object and exe the next() method for each loop.
new_tuple = ("Acura", "Ram", "Honda")  # creates tuple of car brands
for x in new_tuple:  # starts loop to iterate through
    print(x)  # prints every item in tuple by name


the_str = "python"  # creates string 'python'
for x in the_str:  # loops through the string
    print(x)  # prints the string 'python' by line

""" To create class/object as an iterator, you have to implement the __iter__() and 
 __next__() methods to the class/object.
 __iter__() acts similar to __init__() - can do operations like initializing but must return
 the iterator object itself.
 __next__() method allows operations as well but must return the proceeding item in sequence."""


class Numbers:  # A class to create an iterator that doubles the value at each iteration. Starts at 1
    def __iter__(self):  # The __iter__ method is used to initialize the iterator.
        self.x = 1  # Inits iterator stars with 1 as first num in seq
        return self  # returns iterator object, this being self

    def __next__(self):  # __next__ method returns the current number (1 on the first time)
        # on the sequence and doubles for next iteration
        a = self.x  # saves current num before its doubled to return
        self.x *= 2  # doubles value of current number
        return a  # return og current numb before it was doubled


init_instance = Numbers()  # initializes an instance of the class numbers
the_iter = iter(init_instance)  # creates iterator from the numbers instance

print(next(the_iter))  # prints each iteration. Value doubles at each iteration
print(next(the_iter))
print(next(the_iter))
print(next(the_iter))
print(next(the_iter))
print(next(the_iter))
print(next(the_iter))
print(next(the_iter))
print(next(the_iter))

# StopIteration stops iterations from going on forever if in a loop.
# Will raise error if done certain amt of times.


class NewNumbers:  # creates class called NewNumbers
    def __iter__(self):  # initializes the iterator
        self.a = 1  # iterator starts at 1
        return self

    def __next__(self):  # returns current number on the sequence and doubles for next iteration
        if self.a <= 2048:  # if returned value is less than or equal to 2048, double it
            y = self.a
            self.a *= 2
            return y  # outputs value
        else:
            raise StopIteration  # stops iteration if condition is met


newinstance = NewNumbers()  # initializes instance of class NewNumbers
new_iter = iter(newinstance)  # creates iterator from NewNumbers instance

for x in new_iter:  # iterates over the entirety of new_iter
    print(x)  # each element that new_iter gens is printed--a seq of nums starting at 1, doubling til 2048
