import datetime  # imports datetime module

x = datetime.datetime.now()  # gets the current date and time
print(x)  # prints x in YYYY-MM-DD HH:MM:SS.MCROSEC format

y = datetime.datetime.now()
print(y.year)  # prints the year of y
print(y.strftime("%A"))  # prints the current day of y

# create a date using datetime() class - constructor of datetime module.
# datetime() require 3 parameters - year, month, and day.
z = datetime.datetime(2023, 1, 1)
print(z)

a = datetime.datetime(1968,6,1, 12, 38, 55, 123456)
print(a.strftime("%A"))  # Weekday full name
print(a.strftime("%a"))  # Weekday short name
print(a.strftime("%B"))  # month full name
print(a.strftime("%b"))  # month short name
print(a.strftime("%c"))  # Local version of date and time
print(a.strftime("%C"))  # Century
print(a.strftime("%d"))  # day of month
print(a.strftime("%f"))  # Microseconds
