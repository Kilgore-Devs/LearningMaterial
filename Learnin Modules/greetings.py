import module  # imports module.py

a = module.person1['name']  # access the person1 dictionary
print(a)  # prints a which equals 'name'

import module as mx  # give alias when import module

b = mx.person1["age"]  # access the person1 dictionary
print(b)  # prints b which is age

import platform  # imports the built-in module platform

x = platform.system()  # access system being used
print(x)  # prints x which is system info

y = dir(platform)  # dir will return a list of all attributes and method for the object 'platform' module
print(y)  # prints the dir list of various system info

from module import person1  # imports on the person1 from module.py

print (person1["age"])