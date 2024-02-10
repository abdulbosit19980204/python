# Django - Create Virtual Environment


# Virtual Environment

# It is suggested to have a dedicated virtual environment for each Django project, and one way
# to manage a virtual environment is venv, which is included in Python.

# The name of the virtual environment is your choice, in this tutorial we will call it "myworld"

# Type the following in the command prompt, remember to navigate to where you want to create your project

# Windows
# py -m venv myworld

# Unix/MacOS:
# python -m venv myworld

# This will set up a virtual environment, and create a folder bamed "myworld" with subfolders and files, like this:
"""
myworld
    Include
    Lib
    Scripts
    pyvenv.cfg
"""

# Then you have to activate the environment, by typing this command:

# Windows:
# myworld\Scripts\activate.bat

# Unix/MacOS:
# source myworld/bin/activate

# Note: You must activate the virtual environment every time you open the command prompt to work on your project
