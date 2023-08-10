# a dictionary can contain a dictionary. called nested dictionaries.
mycars = {
    "car1": {
        "make": "Ford",
        "model": "Mustang"
    },
    "car2": {
        "make": "Acura",
        "model": "MDX"
    },
    "car3": {
        "make": "BMW",
        "model": "M3"
    }
}

# create three dictionaries then create one that will have the other 3 dictionaries.
kid1= {
    "name": "Ben",
    "age":  3
}
kid2 = {
    "name": "Tom",
    "age":  4
}
kid3= {
    "name": "Mel",
    "age":  5
}
thefam = {
    "kid1": kid1,
    "kid2": kid2,
    "kid3": kid3
}

print(thefam["kid1"])  # accesses kid1 from thefam dictionary
print(mycars["car3"]["model"])  # accesses car3 model
print(mycars.get("car1"))