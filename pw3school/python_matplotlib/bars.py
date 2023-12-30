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

# The bar() function takes arguments that describes the layout of the bars
# The categories and their values represented by the first and second arguments as array
titles = np.array(["apples", "bananas", "oranges", "grapes"])
price = np.array([8000, 15000, 40000, 15000])
plt.bar(titles, price)
plt.show()

# Horizantal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function
# Draw 4 horizantal bars
titles = np.array(["usd", "eur", "gbp", "rub", "riyal"])
differences = np.array([12.250, 13.250, 13.350, 1.250, 8.157])
plt.barh(titles, differences)
plt.show()

# Bar Color
# The bar() and barh() take the keyword argument color the set the color of the bars
plt.barh(titles, differences, color='green')
plt.show()
plt.bar(titles, differences, color='red')
plt.show()

# Bar width
# The bar() takes the keyword argument width to set the width of the bars
# Draw very thin bars
plt.bar(titles, differences, width=0.2, color='#001122')
plt.show()

# The default width value is 0.8
# Note: The horizontal bars, use height insted of width
# Bar height
# The barh() takes the keyword argument height to set the height of the bars
plt.barh(titles, differences, height=0.2, color='#321454')
plt.show()

