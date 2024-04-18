from fastapi import FastAPI
import uvicorn

app = FastAPI()

data = [
    {'id': 1, "name": 'Ali', 'age': 23},
    {'id': 2, "name": 'Vali', 'age': 30},
    {'id': 3, "name": 'Gani', 'age': 18},
    {'id': 4, "name": 'Alisher', 'age': 20}
]


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/all-users/')
async def all_users():
    return {"data": data}


@app.get('/user/{id}/')
async def get_by_user(id: int):
    for user in data:
        if user['id'] == id:
            return user
    return {"message": "{} Not Found".format(id)}


@app.post('/user/create/')
async def create_user(name: str, age: int):
    id = data[-1]['id'] + 1
    data.append({'id': id, 'name': name, 'age': age})
    return {"message": data[-1], 'status_code': 201, 'detail': 'User Created'}


@app.put('/user/{id}/')
async def update_user(id: int, name: str, age: int):
    for user in data:
        if user['id'] == id:
            user['name'] = name
            user['age'] = age
            return {"message": user}
    return {"message": "User Not Found"}


@app.patch('/user/{id}/')
async def update_user(id: int, name: str):
    for user in data:
        if user['id'] == id:
            user['name'] = name
            return {"message": user}
    return {"message": "User Not Found"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
