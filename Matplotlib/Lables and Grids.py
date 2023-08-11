import numpy as np
import matplotlib.pyplot as plt

# creating labels for x and y axis and changing font
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([330, 30, 330, 30, 330, 30, 330, 30, 330, 30])

font1 = {'family': 'cursive', 'color': 'red', 'size': 25}  # changing font and color
font2 = {'family': 'fantasy', 'color': 'blue', 'size': 25}
font3 = {'family': 'monospace', 'color': 'limegreen', 'size': 10}

plt.title("This is the title", fontdict=font1, loc= 'right')  # setting title
plt.xlabel("This is the x axis", fontdict=font3, loc= 'left')  # setting x axis label
plt.ylabel("This is the y axis", fontdict=font2, loc= 'top')  # setting y axis label

plt.plot(x, y)
plt.grid(color = 'red' , linestyle = '--', linewidth = .69)  # adds grid. can specify which gridlines via plt.grid(axis = 'x or y')
plt.show()
