# Matplotlib Markers

# Markers
# You can use the keyword argument marker to emphasize each point with a specified marker
# Mark each point with a circle
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker='o')
plt.show()

# Mark each point with a star '*'
plt.plot(ypoints, marker='*')
plt.show()

# Marker Reference
# You can choose any of these markers
plt.plot(ypoints, marker='o')
plt.show()
plt.plot(ypoints, marker='*')
plt.show()
plt.plot(ypoints, marker='.')
plt.show()
plt.plot(ypoints, marker=',')
plt.show()
plt.plot(ypoints, marker='x')
plt.show()
plt.plot(ypoints, marker='X')
plt.show()
plt.plot(ypoints, marker='+')
plt.show()
plt.plot(ypoints, marker='P')
plt.show()
plt.plot(ypoints, marker='s')
plt.show()
plt.plot(ypoints, marker='D')
plt.show()
plt.plot(ypoints, marker='d')
plt.show()
plt.plot(ypoints, marker='p')
plt.show()
plt.plot(ypoints, marker='2')
plt.show()
# ...

# Format String fmt
# You can also use the  shortcut string  notation parameter to specify the marker
# This parameter is also called  fmt, and is written with this syntax
# marker|line|color
# Mark each point with a circle

plt.plot(ypoints, 'o:r')
plt.show()
# The marker value can be anything from the Marker Reference above
# The line value can be one of the following
# Line Reference
# '_' - Solid line
# ':' - Dotted line
# '--' - Dashed line
# '-.' - Dashed/dotted line

# Note if you leave out the line value in the fmt parameter, no line will be plotted

# Color Reference
# The short color value can be one of the following
# 'r' - Red
# 'g' - Green
# 'b' - Blue
# 'c' - Cyan
# 'm' - Magenta
# 'y' - Yellow
# 'k' - black
# 'w' - White

# Marker Size
# You can use the keyword argument markersize or the shorter version, ms to set the size of the markers
# Set the size of the markers to 20
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20)
plt.show()

# Marker Color
# You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers
# Set the EDGE color red
plt.plot(ypoints, marker='o', ms=20, mec='r')
plt.show()

# You can use markerfacecolor or the shorter mfc to set the color inside the edge of the markers
plt.plot(ypoints, marker='o', ms=20, mfc='r')
plt.show()

# Use the both the mec and mfc arguments to color the entire marker
plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r')
plt.show()

# You can also use Hexadecimal color values
# Mark each point with a beautiful green color
plt.plot(ypoints, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50')

# or any of the 140 supported color names
plt.plot(ypoints, marker='o', ms=20, mec='hotpink', mfc='hotpink')
