# Request Body and Path Parameters

# You can declare path parameters and request body at the same time

# FastAPI will recognize that the function parameters that match path parameters should be taken from the path and that
# function parameters that are declared to be pydantic models should be taken from the request body

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# This way, you can declare path parameters and JSON request bodies, and FastAPI will take care of doing all the data
# validation, serialization, and documentation for you. You could verify it by going to the same API documentation for you

# You could verify it by going to the same API documentation at/docs or by using other tools like Postman with a graphical
# interface or Curl in the command line

# In a similar way, you can declare more complex requests bodies, like list, and other types of request data, like query
# parameters, cookies, headers, from inputs, files, and so on

