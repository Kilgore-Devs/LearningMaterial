from random import *
tank_gallons = randint(10, 25)
miles_on_full = randint(200, 400)

print("The vehicle has " + str(tank_gallons) + " gallons per tank and can drive for " + str(miles_on_full) + " miles.")
print("So that means it has approximately " + str(miles_on_full//tank_gallons) + " miles per gallon.")
