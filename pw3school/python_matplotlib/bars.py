# matplotlib Bars
# Creating Bars
# With pyplot, you can use the bar() function to draw bar graphs
# Draw 4 bars
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([10, 20, 8, 12])
plt.bar(x, y)
plt.show()

