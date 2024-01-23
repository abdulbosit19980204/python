# Use the pydantic Model

# Inside the function, you can access all the attributes of the model object directly

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# The parameter item is declared as an instance of the class Item, and FastAPI will make sure that you recive
# exactly that in your function instead of a dictionary or something else

