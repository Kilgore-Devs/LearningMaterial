# try let you test a code block for errors
# block lets you handle error
# else lets you exe code when there isn't an error
# finally lets you exe even if error
# when error occurs, python stops and prints error message, 'try' handles this

try:
    print(a)  # prints 'a' which isn't defined. raises an error and the except block is exe.
except:  # handles error by printing
    print("Exception has occurred.  :(")

# using multiple exceptions
try:
    print(b)  # prints b which isn't defined.
except NameError:  # try block raises NameError. If a different error then the next except block
    print("The variable is not defined. :(")
except:
    print("A different error occurred.  :(")

# Else is used to define a block of code to exe if no errors raised.
try:
    print("Howdy.")
except:
    print("Something messed up! :(")
else:
    print("There's nothing wrong here.  :)")

# Finally block will be executed if a block raises an error or not, if specified.
try:
    print(x)
except:
    print("Something else is wrong.  :(")
finally:
    print("The try and 'except' blocks are completed.  :)")


# Example of try to open and write a file that isn't writable. Pgm will continue without leaving the .txt file open.
try:
  f = open("nowritefile.txt")
  try:
    f.write("I am writing in the file")
  except:
    print("You do not have the ability to write in this file.  :(")
  finally:
    f.close()
except:
  print("Failed to open file.  :(")

# You can raise an exception if a condition occurs. To throw an exception use 'raise'
y = -20
if y < 0:
    raise Exception("Sorry, the number has to be above 0.")  # raises error, completes everything else that's above.

z = "Hi"
if not type(z) is int:
    raise TypeError("Use only integers.")  # will raise a type error if x  is not an integer
