import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])  # plot 1
y = np.array([3, 2, 1, 0])


plt.subplot(1, 2, 1)  # plots plot 1 (1 row, 2 columns, 1st plot)
plt.plot(x, y)

x = np.array([3, 2, 1, 0])  # plots plot 2
y = np.array([0, 1, 2, 3])

plt.subplot(1, 2, 2)  # plots plot 2 (1 row, 2 columns, 2nd plot)
plt.plot(x, y)

plt.show()
# plots on top of each other
plt.subplot(2, 1, 1)  # 2 rows, 1 column 1st plot
plt.title("Top Plots")  # giving title to plot 1
plt.subplot(2, 1, 2)  # 2 rows, 1 column 2nd plot
plt.title("Bottom Plots")  # giving title to plot 2

plt.suptitle("***These are my plots***")
plt.show()

