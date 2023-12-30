# Matplotlib Scatter

# Creating Scatter Plots
# With Pyplot, you can use the scatter() function to draw a scatter plot
# The scatter function plots ine dot for each obseravation. It needs two arrats of the same lenth,
# one for the values of the x-axis, and one for the y-axis.
# A simple scatter plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y)
# plt.grid()
plt.show()

# The observation in the example above is the result of 13 cars parsing by
# The x-axis shows how old the car is.
# The y-axis shows the speed of the car when it passes
# Are there any relationships between the observations?
# It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registred 13 cars

# Compare Plots
# In the example above, there seems to be a relationship between speed and age,
# but what if we plot the observations from another day as well? Will the scatter plot tell us something else?
#  Draw two plots on the same figure

# day one, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y)

# day two, the age and speed of 15 cars:
x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x, y)

plt.show()

# The two plots are plotted with two different colors, by defaykt blue and orange, you will learn how to change colors
# later in this chapter

# By comparing the two plots, I think it is safe to say that they both gives us the same conclusion:
# the newer the car, the faster it drives

# Colors
# You can set your own color for each scatter plot withe the color or the c argument
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y, color='hotpink')

x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x, y, color='#88c999')

plt.show()

# Color Each Dot
# You can even set a specific color for each dot by using an array of colors as a value for the c argument
# Note: You can't use the color argument for this, only the c argument
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array(
    ["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan",
     "magenta"])

plt.scatter(x, y, c=colors)

plt.show()

# Color Map
# The Matplotlib module has a number of available colormaps
# A colormap is a like a list of colors, where each colors has a value that ranges from 0 to 100
# How to use the colormap
# You can specify the colormap with the keyword argument 'cmap' with the value of the colormap, in this  case 'viridis'
# which is one of the built-in colormaps available in Matplotlib

# In addition you have to create an array with values (from 0 to 100), one value for each point in the scatter plot

# Create a color array, and specify a colormap in the scatter plot
x = np.array([1, 5, 7, 8, 9])
y = np.array([3, 6, 8, 10, 18])
colors = np.array([0, 10, 20, 30, 40])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.show()

# You can include the colormap in the drawing by including  the plt.colorbar() statement
# Include the actual colormap

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

# Available Colormaps
# You can choose any of the built-in colormaps
"""
Name		 	Reverse	
Accent		 	Accent_r	
Blues		 	Blues_r	
BrBG		 	BrBG_r	
BuGn		 	BuGn_r	
BuPu		 	BuPu_r	
CMRmap		 	CMRmap_r	
Dark2		 	Dark2_r	
GnBu		 	GnBu_r
......................
"""

plt.scatter(x, y, c=colors, cmap='Blues')
plt.colorbar()
plt.show()

# Size
# You can change the size of the dots with the s argument
# Just like colors, make sure the array for sizes has the same length as the arrays for the x-axis and y-axis
# Set, your own size for the markers
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])

plt.scatter(x, y, s=sizes)

plt.show()

# Alpha
# You can adjust the transparency of the dots with the alpha argument
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis
# Set your own size for the markers
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

# Combine Color size and alpha
# You can combine a colormap with the different sizes of the dots. This is best visualized if the dots are transparent
# Create random arrays with 100 values for x-points, y-points, colors and sizes
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar(orientation='horizontal')
plt.show()


