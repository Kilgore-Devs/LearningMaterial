my_string = "North Carolina"
print(my_string.rjust(17))
print(my_string.ljust(17, "*"))
center_me = my_string.center(16, "+")
print(center_me)
print(my_string.lstrip("North"))
print(center_me.rstrip("+"))
print(center_me.strip("+"))
print(my_string.replace("North", "South"))


print(len(center_me))
