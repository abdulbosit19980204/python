# Request Body: Receiving JSON Data

# When you need to send data from a client to your API, you send it as a request body

# A request body is data sent by the client to your API.
# A response body is the data your API sends to the client.
# Your API almost always has to send a response body.
# But clients don’t necessarily need to send request bodies all the time.

# Use pydantic to Declare JSON Data Models (Data Shapes)
# First, you need to import BaseModel from pydantic and then use it to create subclasses defining the schema,
# or data shapes, you want to receive.

# Next, you declare your data model as a class that inherits from BaseModel,
# using standard Python types for all the attributes:

# main.py

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
