# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World it is running"}


@app.post("/")
async def root():
    return {"message": "Accepted"}


@app.get('/docs')
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def root():
    return {"message": "Post"}


@app.put("/")
async def root():
    return {"message": "Post"}


@app.delete("/")
async def root():
    return {"message": "Post"}


@app.options("/")
async def root():
    return {"message": "Post"}


@app.head("/")
async def root():
    return {"message": "Post"}


@app.patch("/")
async def root():
    return {"message": "Post"}


@app.trace("/")
async def root():
    return {"message": "Post"}


@app.get("/items/{item_id}")
async def red_item(item_id):
    return {"item_id": item_id}


@app.get("/items/int/{item_int_id}")
async def red_item(item_int_id: int):
    return {"item_id": item_int_id}
