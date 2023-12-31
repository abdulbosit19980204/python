# Matplotlib Pie Chart

# Creating Pie Charts

# With Pyplot, you can use the pie() function to draw pie charts
# A simple pie chart
import matplotlib.pyplot as plt
import numpy as np

y = np.array([11, 5, 22, 1])
plt.pie(y)
plt.show()

# As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [11, 5, 22, 1])

# By default the plotting of the first wedge starts from the x-axis and moves counterclockwise
y = np.array([1, 2, 3])
plt.pie(y, labels=["test1", "test2", "test3"])
plt.show()

# Note: The size of wedge is determined by comparing the value with all the other values, by using this formula:
# The value divided by the sum of all values: x/sum(x)

# Labels
# Add labels to the pie chart with the label parametr
# The label parameter must be an array with one label for each wedge

# A simple pie chart
y = np.array([25, 15, 55, 123])
titles = ["Apple", "Banana", "Cherry", "Peach"]
plt.pie(y, labels=titles)
plt.show()

# Start Angle
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifiying a startangle
# parameter. The startangle parameter is defined with an angle in degrees, default angle is 0
# Start the first wedge at 90 degrees
plt.pie(y, labels=titles, startangle=90)
plt.show()

# Explode
# Maybe you want one  of the wedges to stand out ? The explode parameter allows you to do that
# The explode parameter, if specified, and not None, must be an array with one value for each wedge
# Each value represents how far from the center each wedge is displayed
# Pull the "Apples" wedge 0.2 from the center of the pie
explodeSizes = [0.2, 0, 0, 0]
plt.pie(y, labels=titles, explode=explodeSizes)
plt.show()

# Shadow
# Add a shadow to the pie chart by setting  the shadows parameter to True
plt.pie(y, labels=titles, explode=explodeSizes, shadow=True)
plt.show()

# Colors
# You can set the color of each wedge with the colors parameter
# The colors parameter, if specified, must be an array with one value for each wedge

mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=titles, explode=explodeSizes, shadow=True, colors=mycolors)
plt.show()

# Legend
# To add a list of explanation for each wedge, use the legend() function
plt.pie(y, labels=titles, explode=explodeSizes, shadow=True)
plt.legend()
plt.show()

# Legend With header
# To add a header to the legend, add the title parameter to the legend function
# Add a legend with a header
plt.pie(y, labels=titles, explode=explodeSizes, shadow=True)
plt.legend(title="Fruits")
plt.show()


