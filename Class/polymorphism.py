# Define len() method on different data types
x = "This is python!"  # Define a string variable called x.
print(len(x))  # The len() function returns the length of the string,
# counting each character including spaces and punctuation.

# Tuples are used to store multiple items in a single variable.
tup = ("apple", "orange", "banana")
print(len(tup))  # For tuples, len() function returns the total number of items inside the tuple, in this case, 3 items.

# Dictionaries are used to store data values in key:value pairs.
adict = {"brand": "Ford", "model": "F-150", "year": 2023}
print(len(adict))  # In the context of dictionaries, len() function counts the total number of key-value pairs.


# The classes below demonstrate how different data types can have the same method name (Polymorphism)


class Animal:
    def __init__(self, kind, weight):  # __init__ is a reserved method in python classes (constructor)
        # which is automatically called when a new object of a class is instantiated.
        self.type = kind  # "type" and "weight" are instance variables unique to each instance
        self.weight = weight

    def move(self):  # Define method 'move' for the class 'Animal'
        print("Pets")  # Just prints 'Pets'


class Car:
    def __init__(self, brand, model):  # Define __init__ method for the 'Car' class, with brand and model as parameters
        self.brand = brand
        self.model = model

    def move(self):  # Define method 'move' for the class 'Car'
        print("Drive fast.")  # Just prints 'Drive fast.'


class Truck:
    def __init__(self, brand, model):  # Define __init__ method for the 'Truck' class,
        # with brand and model as parameters
        self.brand = brand
        self.model = model

    def move(self):  # Define method 'move' for the class 'Truck'
        print("Tow stuff.")  # Just prints 'Tow stuff.'


# Instantiate instances of the classes


animal = Animal("Dog", 60)  # Create new animal
car = Car("Ferrari", "Spyder")  # Create new car
truck = Truck("Ram", 1500)  # Create new truck

for x in (animal, car, truck):  # Apply 'move' function on the instances
    x.move()  # In python, you can use the same operation for different types of objects.


# The classes below demonstrate how polymorphism can be used in inheritance.


class Vehicle:
    def __init__(self, make, model):  # Constructor method for Class 'Vehicle'
        self.make = make
        self.model = model

    def move(self):  # Define 'move' method for the class 'Vehicle'
        print("move")  # Just prints 'move'


# 'Motorcycle' class inherits from 'Vehicle' class.
# All properties and methods of 'Vehicle' become available to 'Motorcycle'
class Motorcycle(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):  # We override the 'move' method of 'Vehicle' inside 'Boat'
        print("on the water")  # Just prints 'on the water'


class Airplane(Vehicle):
    def move(self):  # We override the 'move' method of 'Vehicle' inside 'Airplane'
        print("in the sky.")  # Just prints 'in the sky.'


# Instantiate objects for each class
motorcycle = Motorcycle("HD", "Sportster")  # Create new motorcycle
boat1 = Boat("DeepSea", "Sailboat")  # Create new boat
plane = Airplane("USAF", "C-130")  # Create new airplane

for x in (motorcycle, boat1, plane):  # Apply 'move' function on the instances
    print(x.make)  # Print the make of each 'Vehicle'
    print(x.model)  # Print the model of each 'Vehicle'
    x.move()  # Call the move method for all classes
