import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 8, 10, 8, 5, 4, 3, 2, 1])
y = np.array([1, 2, 3, 4, 5, 20, 50, 80, 95, 96, 97, 98, 99])
plt.scatter(x, y, color='black')  # can change color of plots with name or hex value
# can add a second set to compare
x = np.array([2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2])
y = np.array([1, 2, 3, 4, 5, 20, 50, 80, 95, 96, 97, 98, 99])
plt.scatter(x, y, color='red')  # can change color of plots with name or hex value

plt.show()