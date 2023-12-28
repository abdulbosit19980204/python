# Create Labels for a Plot
# With PyPlot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

# Create a title for a Plot
# With PyPlot, you can use the title() function, to set a title for the plot

plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Testing")
plt.show()

# Set Font Properties for Title and Labels
# You can use the fontdict parameter in xlable, ylabel and title to set font properties for the title and labels
plt.plot(x, y)
font1 = {'family': 'sans-serif', 'color': 'red', 'weight': 'bold', 'size': 20}
font2 = {'family': 'sans-serif', 'color': 'blue', 'weight': 'normal', 'size': 15}
plt.title('Testing', fontdict=font1)
plt.xlabel("x-axios", fontdict=font2)
plt.ylabel("y-axios", fontdict=font2)
plt.show()

# Position the Title
# You can use the loc parameter in title() to position the title

# Legal values are 'left', 'right', and 'ceneter'. Default value is 'center'
plt.plot(x, y)
plt.title("Testing", fontdict=font1, loc='left')
plt.show()

