# Machine Learning - Mean Median Mode

# What can we learn from looking at a group of numbers
# In Machine Learning (and in mathematics) there are often three values that interestes us

# Mean - the average value
# Median - The mid point value
# Mode - The most common value

# Example: We have registered the speed of 13 cars:
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
# What is the average, the middle, or the most common speed value?

# Mean
# The mean value is the average value
# To calculate the mean, find the sum of all values, and divide the sum by the number of values
# (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77
# The NumPy module has a method for this.
# Use the NumPy mean() method to find the average speed
import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.mean(speed)
print(x)

# Median
# The median value is the value in the middle, after you have sorted all the values
# 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111 === 87 is the median value
# It is important that the numbers are sorted before you can find the median

# The numpy module has a method for this

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.median(speed)
print(x)

# Mode
# The mode value is the value that appears the most number of times
# 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86
# The SciPy module has a method for this.
# Use the SciPy mode() method to find the number that appears the most
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 87, 86]

x = stats.mode(speed)

print(x)

# Chapter Summary
# The Mean, Median, and Mode are techniques that are often used in Machine Learning, so it is important to understand
# the concept behind them

