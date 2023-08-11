# Histograms show frequency distributions. Shows number of observations within given intervals.
# hist()
import matplotlib.pyplot as plt
import numpy as np

# create random numbers that concentrate around 170, STDv of 10 and 250 values
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
