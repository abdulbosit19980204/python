# First Step

# The simplest FastAPI file could look like this:
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Run the live server:
# uvicorn main:app --reload

# Note:
# The command uvicorn main:app refers to
# main: the file main.py (the Python "module")
# app: the object created inside of main.py with the line app=FastAPI()
# -- reload: make the server restart after code changes. Only use for development

# In the output, there is a line with something like:
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

# That line shows the URL where your app is being served, in your local machine

# Check it

# Open your browser at http://127.0.0.1:8000/
# You will see the JSON response
# {"message": "Hello World"}


# Interactive API docs
# Now go to http://127.0.0.1:8000/docs

# Alternative API docs
# And now, go to http://127.0.0.1:8000/redoc

# OpenAPI
# FastAPI generates a "schema" with all your API using the OpenAPI standart for defining APIs.

# "Schema"

# A "schema" is a definition or description of something. Not the code that implements it,
# but just an abstract description

# API "schema"
# In this case, OpenAPI is a specification that dictates how to define a schema of your API.
# This schema definition includes your API paths, the possible parameters they take, etc.

# Data "schema"
# The term "schema" might also refer to the shape of some data, like a JSON content.
# In that case, it would mean the JSON attributes, and data types they have, etc.

# OpenAPI and JSON schema
# OpenAPI defines an API schema for your API. ANd that schema includes definitions (or "schemas") of the data sent
# and received by your API using JSON Schema, the standard for JSON data schema.

# Check the openapi.json
# If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with
# the description of all your API.
# You can see it directly at: http://127.0.0.1:8000/openapi.json
# It will show a JSON starting with something like:

"""
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {



...
"""

# What is OpenAPI

# The OpenAPI schema is what powers the two interactive documentation systems included.
# And there are doznes of alternatives, all based on OpenAPI. You could easily add any of those alternatives to
# your application built with FastAPI

# You could also use it to generate code automatically, for clients that communicate with your API.
# For example, frontend, mobile or IoT applications
