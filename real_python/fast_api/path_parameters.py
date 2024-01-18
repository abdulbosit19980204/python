# Path parameters: Get an Item By ID

# You can declare path parameters or variables with the same syntax used by Python foramatted string
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def red_item(item_id):
    return {"item_id": item_id}


# The value of the path parameter item_id will be passed to your function as the argument item_id

# So if you run this example and go to http://127.0.0.1:8000/items/foo, you will see this response
# {"item_id": "foo"}

# The response containes "foo", which is what was passed in the item_id path parameter and then returned in a dictionary.

# Path parameters with Types

# You can declare the type of path parameter in the function using standard Python type hints
@app.get("/items/{item_id}")
async def red_item(item_id: int):
    return {"item_id": item_id}


# In this case, you declare item_id to be an int
# Declaring the type of a path parameter will give you editor support inside of your function, with error checks, completion

# Data Conversion
# If you run the above example and navigate your browser to http://localhost:8000/items/3 then you will see the following res
{"item_id": 3}

# Notice that the value your function received and then returned is 3 which is a Python int, not a string ("3").
# So, with that type declaration, FastAPI gives you automatic "request parsing"

# Data Validation
# If you point your browser to http://127.0.0.1:8000/items/foo, then you will see a nice HTTP error:
"""
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
"""

# This is because the path parameter item_id has a value of "foo", which is not int

# The same error would appear if you provide a float instead of an int, such as if you opened http://127.0.0.1:8000/items/4.2
# in your browser. So with the same Python type hint, FastAPI gives you both data parsing and data validation

# Also notice that the error clearly states the exact point where the validation didn't pass. This is incredibly helpful
# while developing and debugging code that interacts with your API

# Documentation
# When you open your browser at http://127.0.0.1:8000/docs , you will see an automatic, interactive API documentation

# Again, with that same Python type declaration,
# FastAPI gives you automatic, interactive documentation integrating Swagger UI.
# Notice that the path parameter is declared to be an integer.

# Because FastAPI is built on top of the OpenAPI standard,
# it also provides an alternative API documentation using ReDoc, which you can access at http://127.0.0.1:8000/redoc:

# Data Handling with Pydantic

# All the data validation is performed under the hood by pydantic, so you get all the benefits from it,
# and you know you are in good hands.

# You can use the same type declarations with str, float, bool and many other complex data types.

# Order Matters: Put Fixed Paths First

# When creating path operations, you may find situations where you have a fixed path, like /users/me.
# Let’s say that it’s to get data about the current user.
# You might also have the path /users/{user_id} to get data about a specific user by some user ID.

# Because path operations are evaluated in order,
# you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Otherwise, the path for /users/{user_id} would also match for /users/me,
# thinking that it’s receiving the parameter user_id with a value of "me".

