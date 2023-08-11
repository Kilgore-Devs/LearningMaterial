import matplotlib.pyplot as plt
import numpy as np

x = np.array(["W", "X", "Y", "Z"])
y = np.array([7, 2, 3, 8])

plt.bar(x, y, width=.1)  # can change width
plt.show()

x = ["Raptor R", "TRX"]
y = [10, 20]
plt.bar(x, y,)
plt.show()

x = np.array(["W", "X", "Y", "Z"])
y = np.array([7, 2, 3, 8])

plt.barh(x, y, color="orange", height=.3)  # .barh means horizontal, can use hex or name for colors,
# change height by using height instead of width
plt.show()
