from fastapi import FastAPI
import uvicorn

posts = [
    {
        "id": 1,
        "title": "O'zbekiston",
        "description": "O'zbekiston kelajagi buyuk davlat",
        "author_id": 2,
    },
    {
        "id": 2,
        "title": "China",
        "description": "China is the country that has the most populous",
        "author_id": 1,
    },
    {
        "id": 3,
        "title": "O'zbekiston2",
        "description": "O'zbekiston kelajagi buyuk davlat",
        "author_id": 3,
    },
    {
        "id": 4,
        "title": "O'zbekiston3",
        "description": "O'zbekiston kelajagi buyuk davlat",
        "author_id": 1,
    }
]

comments = [
    {
        "id": 1,
        "message": "zo'r",
        "post_id": 2
    },
    {
        "id": 1,
        "message": "Ajoyib",
        "post_id": 1
    },
    {
        "id": 1,
        "message": "Wav",
        "post_id": 2
    },
    {
        "id": 1,
        "message": "Zerikarli",
        "post_id": 3
    },
    {
        "id": 1,
        "message": "zo'r",
        "post_id": 4
    },
    {
        "id": 1,
        "message": "zo'r",
        "post_id": 1
    },
    {
        "id": 1,
        "message": "zo'r",
        "post_id": 3
    },
]

authors = [
    {
        "id": 1,
        "name": "Admin",
    },
    {
        "id": 2,
        "name": "Kimdur",
    },
    {
        "id": 3,
        "name": "Bratan",
    }
]
app = FastAPI()


@app.get('/')
async def root():
    return {'Hello': 'World'}


@app.get('/posts')
async def get_posts():
    return {"posts": posts}


async def get_post_info(pk: int):
    for post in posts:
        if post['id'] == pk:
            return post


async def get_author(user_id: int):
    for author in authors:
        if author['id'] == user_id:
            return author


async def get_comments(post_id: int):
    post_comments = []
    for comment in comments:
        if comment['post_id'] == post_id:
            post_comments.append(comment)
    return post_comments


@app.get('/article/{pk}')
async def get_post(pk: int):
    for post in posts:
        if post['id'] == pk:
            aid = post['author_id']
            post_comments = []
            for comment in comments:
                if comment['post_id'] == post['id']:
                    post_comments.append(comment)
            for author in authors:
                if author['id'] == aid:
                    return {"post": post, "author": author, "comments": post_comments}
    return {"message": "Post Not Found"}


@app.get('/posts/{pk}')
async def get_posts(pk: int):
    post = await get_post_info(pk)
    author = await get_author(post['author_id'])
    post_comments = await get_comments(post['id'])
    return {"post": post, "author": author, "comments": post_comments}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
