# What is the PIP?
from pip._internal.distributions import installed

# PIP is a package manager for Python packeges, or modules if you like
# Note: If you have Python version 3.4 or later, PIP included by default

# What is the Package
# A package contains all the fiels you need for a module
# Modules are Python code libraries you can include in your project

# Check if PIP is Installed
# Navigate your command line to the location of Python's script directory, and type the following
# Check the pip version
# pip 23.3.2 from D:\coding\python\venv\Lib\site-packages\pip (python 3.12)

# Install PIP
# If you do not have PIP installed, you can download and install if from this page : https://pypi.org/project/pip/
# Download a Package
# Downloading a package is very easy
# Open the command line interface and tell PIP download the package you want
# Navigate your command line to the location of Python's script directory, and type the following
# Download a package name "camelcase"
# pip install camelcase

# Using a Package
# Once the package is installed, it is ready to use
# Import the "camelcase" package into your project

import camelcase
from requests import packages

c = camelcase.CamelCase()
txt = "hello world and Uzbeksitan"
print(c.hump(txt))  # Hello World and Uzbeksitan

# Find Packages
# Find more packages at  https://pypi.org/.

# Remove a Package
# Use the unistall command to remove a package

# pip unistall camelcase

# Lost Packages
# Use the list command to list all the packages installed on your system

