# Matplotlib Line

# Linestyle
# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line
# Use a dotted line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, ls='dotted')
# plt.plot(ypoints, linestyle='dotted')
plt.show()

# Use a dashed line
plt.plot(ypoints, ls='dashed')
plt.show()

# Shorter Syntax
# The line style can be written in  a shorter syntax
# linestyle can be written as ls
# dotted can be as :
# dashed can be as --

plt.plot(ypoints, ls=':')
plt.plot(ypoints, ls='--')
plt.show()

# Line Color
# You can use the keyword argument color or the shorter c to set the color of the line
plt.plot(ypoints, color='blue')
plt.show()
# You can also use Hexadecimal color values
plt.plot(ypoints, c='#4CAF50')
plt.show()

# Line Width
# You can use the keyword argument linewidth or the shorten lw to changen the width of the line
# The value is a floating number in points
plt.plot(ypoints, lw='20.5')
plt.show()

# Multiple Lines

# You can plot as many lines as you like by simply adding more plt.plot() function

y1 = np.array([1, 5, 7, 8, 11])
y2 = np.array([3, 11, 6, 8, 15])
y3 = np.array([3, 11, 18, 8, 15])
plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

