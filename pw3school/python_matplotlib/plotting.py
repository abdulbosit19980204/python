# Matplotlib Plotting

# Plotting x and y points
# The plot() function is used to draw points(markers) in a diagram
# By default, the plot() function draws a line from point to point
# The function takes parameters for specifying points in the diagram

# Parameter 1 is an array containing the points on the x-aixs
# Parameter 2 is an array containing the points on the y-aixs

# If we need to plot a line from (1,3) to (8,10) we have to pass two arrays [1,8] and [3,10] to the plot function

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, color='red', linewidth=2)
plt.show()

# The x-axis is the horizontal axis
# The y-axis is the vertical axis

# Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'

# Draw two positon in the diagram, one at position (1,3) and one in position (8,10)
plt.plot(xpoints, ypoints, 'o')
plt.show()

# Multiple points
# You can plot as many points as you like, just make sure you have the same number of points in both axis
xpoints = np.array([1, 8, 5, 7, 8, 4])
ypoints = np.array([2, 5, 8, 9, 11, 4])
plt.plot(xpoints, ypoints, color='red', linewidth=2)
plt.show()

# Default X-Points
# If we don't the specify the points on the x-axis, they will get the default values 0,1,2,3...
# depending on the length of the y-points
# So, if we take the same examples as above, and leave out the x-points, the diagram will look like this:
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# The x-points in the example above are [0,1,2,3,4,5]
