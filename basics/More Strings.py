lowercase = "there are no capitol letters here."
print(lowercase.upper())  # prints variable in upper case
print(lowercase)
print(lowercase.isupper())  # returns true/false if upper case
print(lowercase.islower())

uppercase = "THIS IS UPPERCASE."
print(uppercase.lower())  # prints the variable in lower case
print(uppercase)
print(uppercase.isupper())  # returns true/false if lower case
print(uppercase.islower())


print("CAPS".lower().isupper())  # prints CAPS in lowercase and returns fals because it's not upper
print("My name is".isalpha())  # returns false bcause of spaces
print("89765465".isdecimal())  # returns true, false if .123
print("There are spaces here.".isspace())  # returs false because there are more than just spaces
print("There are spaces here."[5].isspace())  # returns true because index 5 is a space

print("this is a string".startswith("t"))  # returns true because the string starts with a 't'
print("this is a string".endswith("g" or "string"))  # returns true because it ends with g or string

print("".join(["1", "2", "3"]))  # put what you want to join with in the first "" - has to be a string
print("One, Two, Three")
print("One, Two, Three".split(", "))

# ,rjust() and .ljust() Justifies by adding spaces
print("Which way is this adjusted".rjust(30))
print("Which way is this adjusted".ljust(30, "*") + " 30 spaces to the left")  # adds fill char *
print("This is centered".center(30, "-"))
print("Which way is this adjusted!!!111".strip("1"))  # can use rstrp and lstrip and strip words
print("redredblackred".strip("der"))  # removes red on each side of string
print("redredblackredred".replace("red", "?")) # replaces red with ?


