cars = ["Ford", "Volvo", "BMW"]  # create an array
x = cars[1]  # get 1st item in array
print(x)  # prints
cars[1] = "Acura"  # modify the second item in array with Acura
print(x)  # prints cars
x = len(cars)
print(x)
for x in cars:  # can loop in arrays
    print(x)
# add 1 more element to the array
cars.append("Honda")
print(cars)
# remove array elements with .pop
cars.pop(0)  # removes first item
print(cars)
# can also use remove
cars.remove("Acura")
print(cars)
