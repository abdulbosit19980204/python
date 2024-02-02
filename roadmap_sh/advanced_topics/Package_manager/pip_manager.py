# PIP

# The standard package manager for Python is pip.
# It allows you to install and manage packages that aren’t part of the Python standard library.

# Running pip as a Module
"""
When you run your system pip dirctly, the command itself doesn't reveal which python version pip belongs to.
This unfortunately means that you could use pip to install a package into the site-packages
of an old Python version without noticing. To prevent this from happening, you cam run pip as Python module
"""

# python3 -m pip

"""Notice that you use python3 -m to run pip. The -m switch tells Python to run a module as an executable of the python3
interpreter.
 Sometimes you may want to be more explicit and limit package to a specific project. In situations lik, this you should
 run pip a virtual environment"""

# Using pip in a Python Virtual Environment

"""
To avoid installing packages directly into your system Python installation, you can use a virtual environment.
A virtual environment provides an isolated Python interpreter for your projet
Any packages that you use inside this environment will be independent of your system interpreter. This means that you can
keep your project's dependencies seperated from other projects and the system at large.
"""
# Using pip inside a virtual environment has three main advantages:

"""
1. Be sure that you're using right Python version for the project at hand
2. Be confident that you're referring to the correct pip instance when running pip or pip3
3. Use a specific package version for your project without affecting other projects
"""
"""
Python 3 has the built-in venv module for creating virtual environments. This module helps you crate virtual environments 
with an siolated Python installation. Once you've activated the virtual environment, the you can install packages into this
environment. The packages that you install into one virtual environment are isolated from all other environments on your system

You can follow these steos to create a virtual environment and verify that you're using the pip module inside the newly 
created environment. 
"""

# python -m venv venv
