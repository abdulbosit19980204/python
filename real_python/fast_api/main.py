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
