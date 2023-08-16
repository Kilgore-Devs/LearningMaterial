# four variables from suer input.
name = input("What is your name?  ")
food = input("What is your favorite food?  ")
car = input("What is your favorite car?  ")
animal = input("What is your favorite animal?  ")
# concatenate them together with additional strings to form a sentence
print("Hello " + name + ". I bet you wish you could be eating " + food + " right now! \n" +
      car + "'s are not that fun. Ride a motorcycle instead. \n" + animal +
      "s are cute. I would like to have a pet " + animal + " someday.")

# to make this easier, call .format() to insert args inside {} ... must use in order.
print("\n\n***Unlike above, this is printed using .format().***\nHello {}. You like {}, {}s, and {}s.".format(name, food, car, animal))
