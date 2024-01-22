# main.py
from fastapi import FastAPI
from pydantic import BaseModel

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


@app.get("/file/{file_path:path}")
async def red_item(file_path: str):
    return {"file_path": file_path}


# from fastapi import FastAPI


class Auth(BaseModel):
    login: str
    password: str


# app = FastAPI()
@app.post("/auth/")


async def create_user(auth: Auth):
    return auth
