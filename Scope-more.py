def func():
    a = 200
    print(a)


func()


def newfunc():
    b = 500

    def innerfunc():  # creates a function inside a function
        print(b)
    innerfunc()


newfunc()


# a variable created in the main body is a global variable
x = 1000  # set global variable x to 1000


def fx():
    x = 300  # defines local variable
    print(x)


fx()  # runs fx function and prints local x

print(x)  # prints global x which is 1000

# global keyword is use in a function to define a global variable


def newfx():
    global x  # set global var x to 2000
    x = 2000


newfx()
print(x)  # prints new global 'x' variable which is 2000
