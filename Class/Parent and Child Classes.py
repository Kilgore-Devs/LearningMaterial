class Person:  # Define a new class called Games.

    def __init__(self, firstname, lastname):  # Define the constructor method (__init__) that inits the class attributes
        self.firstname = firstname  # Assign the value of the 'pc' parameter to the 'self.pc' attribute.
        self.lastname = lastname  # Assign the value of the 'console' parameter to the 'self.console' attribute.

    def printname(self):  # Define a method called printname.
        print(self.firstname, self.lastname)  # Print the values of 'self.pc' and 'self.console' attributes.


x = Person("Amy", "Johnson")  # Create an instance of the Games class with "CoD" as the 'pc' parameter,
# and "Apex" as the 'console' parameter.
x.printname()  # Call the printname method of the x instance,
# which will print the values of the 'pc' and 'console' attributes.


class Student(Person):  # Student class inherits same properties and methods as the Person class
    # pass - Use if you don't want to add properties or methods to the class
    def __init__(self, firstname, lastname):  # when use __init__, child class no longer inherits parents __init__.
        # The childs init overrides the parents init fx. to keep, add a call to parents init_ fx by Person.__init__()
        Person.__init__(self, firstname, lastname)  # <--keeps inheritance of parent's class.


y = Student("Mel", "Gibson")
y.printname()


class Student(Person):  # Student class inherits same properties and methods as the Person class
    def __int__(self, firstname, lastname):
        super().__init__(firstname, lastname)  # <--makes child class inherit all methods and props of parent.
        # When you use super() fx, no need to use name of parent, it auto inherits.
        self.graduationyear = 2023  # <-- Adds a property call graduation year.


z = Student("Alex", "Jackson")
z.printname()


class Student(Person):  # Student class inherits same properties and methods as the Person class
    def __init__(self, firstname, lastname, year):  # year is added as a parameter in the int fx
        super().__init__(firstname, lastname)
        self.gradyear = year


b = Student("Charlie", "Charles", 2023)
b.printname()


class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.gradyear = year

    def welcome(self):  # Adds a method called welcome to the Student class
        print("Welcome", self.firstname, self.lastname, "to the class of", self.gradyear)  # prints parameters


student = Student("Brittany", "Smith", 2023)  # creates instance of Student class
student.welcome()  # calls welcome method to print the message
