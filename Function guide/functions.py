# functions help avoiding using extra lines of code
# print("this")
# print("is")
# print("an")
# print("example")
# if you wanted to print these 4 lines several times without copying and pasting, use function like below
# def prints_four():
#    print("this")
#    print("is")
#    print("an")
#    print("example")
#
# need two blank lines
# prints_four()
# prints_four()
# prints_four()
# prints_four()
# def function_name(): There are five parts to every fx. make names that are obvious to read what they are used for
#    print(2 + 2) code associated with function, must be four spaces
# to call fx, use name followed by ()
# function_name()---calls function
# parameter is a placeholder
# def function_name(parameter): can have as many parameters as want, need , and a space between each
#    print(parameter + 2)
# function_name(8)<--argument in ()
# def default_example(num1=7, num2=8):
#    print(num1 * num2) will print 56
# or  return num1 * num2         if you want to use output ex; below
# def default_example(num1=7, num2=8):
#    return num1 * num2


# print(default_example() + 44)  # adds 44 to returned value of num1 * num2
def name_printer(user_name):
    print(user_name)


name = input("What is your name?")
name_printer(name)
