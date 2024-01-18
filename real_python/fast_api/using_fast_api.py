# Using FAST API to BUILD Python WEB API

# In this tutorial, we'll learn how to:
#     Use path parameters to get a unique URL path per item
#     Receive JSON data in your requests using pydantic
#     Use API best practise, including validation, serialization, and documentation
#     Continue learning about FASTAPI for you use cases

# What Is Fast API?
# Fast API is a modern, high-performance web framework for building APIs with Python based  on standard type hints.
# It has the following key features

# Install FastAPI
# As with any other Python project, it would be best to start by creating a virtual environment.
# If you are not familiar with how to do that, then you can check out the  Primer on Virtual Environments.
# The first step is to install FastAPI and Uvicorn using pip

# python -m pip install fastapi uvicorn[standard]
# With that, you have FastAPI and Uvicorn installed and are ready to learn how to use them.
# FastAPI is the framework you’ll use to build your API, and Uvicorn is the server
# that will use the API you build to serve requests.

# First Steps

# To get start, in this section, you will create a minimal FastAPI app, run it with a server using Uvicorn,
# and then learn all the interacting parts. This will give you a very quick overview of how evrything works

# Create a First API
# A basic FastAPI file looks like this:
# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# This code defines your application, but it won't run on itself if you call it with pytho directly. To run it, you need
# a server program. In the steps above, you already installed Uvicorn. That will be your server

# Run the First API with Uvicorn


# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# The line in the output shows the URL where your app is being served in your local machine. Since you used --reload for
# development, when you update your application code, the server will reload automatically.

# Check the Response

# Open your browser to http://127.0.0.1:8000, which will make your browser send a request to your application. It will
# then send a JSON response with the following :
#     {"message": "Hello World"}

# That JSON message is the same dictionary that you returned from the function in your application. FastAPI takes care
# of serializing the Python dict into JSON object and setting the appropriate Content-Type

# Check the Interactive API Documentation
# Now open http://127.0.0.1:8000/docs in your browser

# You will see the automation interactive API Documentation provided by Swagger UI:
# The browser-based user interface documenting your API is provided and intagrated by default. You don't have to do anything
# else to take advantage of it with FastAPI

# Check the Alternative Interactive API Documentation
# Now, go to http://127.0.0.1:8000/redoc in your browser
# You will see the alternative automatic documentation provided by ReDoc

# As FastAPI is based on standards like OpenAPI, there are many alternative ways to show the API documentation.
# FastAPI provides these two alternatives by default

# The First API, Step by Step
# Now let's analyze that code step by step and understand what each part does.
# Step 1 is to import Fast API

# from fastapi import FastAPI

# FastAPI is a Python class that provides all the functionality for yor API

# Step 2 is to create a FastAPI instance:
# app = FastAPI()
# Here the app variable will be an instance of the class FastAPI. This will be the main point of interaction to create
# your API
# This app is the same one you referred to above in the command to run the live server with uvicorn

# uvicorn main:app --reload

# Before continuing with step 3, it's worth taking a moment to get familiar with a couple of terms. Path referes to the
# last part of the URL starting from the first forward slash character (/). So, in a URL like https://example.com/items/foo
# the path would be /items/foo.
# A path is also commonly called an endpoint or a route, but the term path will be used in this tutorial
# When you're building an API, the path is the main way you can separate resources

# Another important term to know is operation, which is used in reference to any of the HTTP request methods:
"""
POST
GET
PUT
DELETE 
OPTIONS
HEAD
PATCH
TRACE
"""

# With HTTP, you can communicate with each path using one (or more) of these operations.
# Knowing what those two terms mean, you're ready to continue with step three

# Step 3 is to define a path operation decorator

# @app.get("/")

# The @app.get("/") tells FastAPI that the function right below is in charge of handling requests go to the path / using
# a get operation. This is a decorator related to a path operation, or a path operation decorator
# If you want to learn a bit more about decorators, then check out the Primer on Python Decorators

# You can also use the other operations mentioned above
# @app.post("/")
# @app.put("/")
# @app.delete("/")
# @app.options("/")
# @app.head()
# @app.patch("/")
# @app.trace()

# In each case, you would use the appropriate path operation decorator above a function that is in charge of handling
# those requests

# Step 4 is to define the path operation function, or the function that goes below the path operation decorator

# async def root():
# This function will be  called by FastAPI whenever it receives a requests to the specified URL (/) using a Get operation.
# In this case, it is an async function

# You could also define it as a normal function instead of using async def
# def root()

# If you don't know the difference between normal functions and async functions and when to use them, check out
# Concurrency and async/await in the FastAPI documentation

# Step5 is to return the content
# return {"message": "Hello World"}
# You can return a dictionary, list or singular values as string, integers and so on
# You can also return pydantic models, which you'll learn more about later

# There are many other objects and models that will be automatically converted to JSON, including object-relational mappers
# ORMs and others. Try using your favorite ones -it's highly probable that they are already supported

