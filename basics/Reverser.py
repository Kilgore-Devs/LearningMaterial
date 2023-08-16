your_input = input("Input something here:   ")  # assigning user input to a string
rewind = ""  # empty string assigned to the variable rewind. used to store reversed ver of user input

for item in range(len(your_input) - 1, -1, -1):
    rewind += your_input[item]  # input chars at each item index is added to the rewind string - gives the reverse order

print(rewind)
"""
For loop is started. 
Starts at the length of the input string and subtracted by 1 (-1). This is because python index starts at 0, not 1.
Then goes down by 1 (-1) and stops one index before the lower end. 
Indicating the loop is going in reverse starting from the end of the input.
"""