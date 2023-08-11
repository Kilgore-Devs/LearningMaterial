# colorMap
# colors = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])
# plt.scatter(x, y, c=colors, cmap='viridis')
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2])
y = np.array([1, 2, 3, 4, 5, 20, 50, 80, 95, 96, 97, 98, 99])
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])  # creates color array
colors = np.array([100, 90, 80, 70, 60, 50, 40, 50, 60, 70, 80, 90, 100])  # changes sizes


plt.scatter(x, y, c=colors, cmap='magma', s=sizes, alpha=.25)
# changes colors and sizes per above. alpha=0.0-1.0, closer to zero means more transparent.
# for more https://matplotlib.org/stable/tutorials/colors/colormaps.html

plt.colorbar()  # adds color map to the output

plt.show()
