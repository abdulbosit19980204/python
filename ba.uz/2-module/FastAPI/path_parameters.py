# Path Parameters

# You can declare path "parameters" or "variables" with the same syntax used by Python format strings:
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# The value of the path patameter item_id will be passed to your function as the argumet item_id
# So if you run this example and go to  http://127.0.0.1:8000/items/foo, you will see a response of:
# {"item_id":"foo"}

# Path parameters with types

# You can declare the type of a path parameter in the function, using standard Python type annotations.
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# In this case, item_id is declared to be an int.

# Data conversation
# If you run this example and open your browser  at http://127.0.0.1:8000/items/3, you will see a response of:
# {"item_id": 3}

