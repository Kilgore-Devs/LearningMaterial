example = "hello"  # global

def loc_ex():
    examplelocal = "string"  # local
    return example      # local


print(example)  # global
print(examplelocal)  # local and will error to function above
print(loc_ex())  # global
