import matplotlib
import matplotlib.pyplot as plt  # imports pyplot as alias plt
import numpy as np
print(matplotlib.__version__)  # The __version__ attribute stores the the version string.

xpoints = np.array([0, 100])
ypoints = np.array([0, 256])

plt.plot(xpoints, ypoints)
plt.show()

xpoints = np.array([3, 8])
ypoints = np.array([5, 10])

plt.plot(xpoints, ypoints)  # draws a line
plt.show()

xpoints = np.array([3, 8])
ypoints = np.array([5, 10])

plt.plot(xpoints, ypoints, 'x')  # use the string x to plot a marker, can use others.
plt.show()

xpoints = np.array([0, 9, 6, 1, 12, 15])  # draws a line from (0,10), (9, 8), (6, 6) and so on.
ypoints = np.array([10, 8, 6, 4, 2, 14])

plt.plot(xpoints, ypoints)
plt.show()

xpoints = np.array([10, 8, 6, 4, 2, 14])  # if you don't specify x,points they will be 0, 1, 2, 3...
plt.plot(ypoints)
plt.show()

ypoints = np.array([2, 10, 4, 8, 6])

plt.plot(ypoints, marker='*')  # use keyword marker to pick what to mark with
plt.show()
