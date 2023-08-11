import matplotlib.pyplot as plt
import numpy as np

y = np.array([30, 10, 45, 15])  # starts at first wedge on right going counterclockwise. Default angle is 0.
thelabels = ["Carbs", "Fats", "Protein", "Fiber"]
pullawayfrompie = [.1, .1, .5, .1]  # explode is used in plt.pit to pull pieces out.
thecolors = ["Bisque", "Yellow", "Brown", "SeaGreen"]

plt.pie(y, labels=thelabels, startangle=90, explode=pullawayfrompie, shadow=True, colors=thecolors)
plt.legend(title = "Daily Consumption")  # adds a legend, and title inside()
plt.show()





