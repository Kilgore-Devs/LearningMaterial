mixed_case = "The Incredible Hulk"
print(mixed_case.isupper())  # Use isupper to check if mixed_case is string of all upper case letters & print result
print(mixed_case.islower())  # Use islower to check if mixed_case is string of all lower case letters & print result
print(mixed_case.upper())  # Change all letters in mixed_case to upper case letters using upper and print result
print(mixed_case.lower())  # Change all  letters in mixed_case to lower case  using lower and print result
print(mixed_case.istitle())  # Use the istitle method to check if mixed_case is title case and print result
title_case = mixed_case.title()  # Make a var called title_case and assign it the result of title being called on mixed_case
print(title_case)  # print title case
print(mixed_case.startswith("A"))  # call statswith on mxd case with the letter mxd case starts with as an arg. print it
print(mixed_case.endswith("e"))  #
words = mixed_case.split()  #
print(words)  #
print("".join(words).isalpha())
"""Use join method to join  all of 
the items in the list assigned to words as a single string.  
Use isalpha to check if the string is made up entirely of letters.  
Lastly, use print to display results."""
