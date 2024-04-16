# Concurrency and Async await

# Details about the async def syntax for path operation functions and some background about asynchronous code,
# concurrency, and parallelism.


# In a hurry?
# If you are using third party libraries that tell you to call them with await, like.
@app.get('/')
async def read_result():
    result = await some_library()
    return result


# You can only use await inside of function created with async def.

# If you are using a third party library that communicates with something (a database, an API, the filesystem, etc.) and
# doesn't have support for using await, (this is currently the case for most database libraries), then declare your path
# operation function as normally, with just def, like.

@app.get('/')
def result():
    result = sone_library()
    return result

# If your application (somehow) doesn't have communicate with anything else and wait for it to respond, use async def.
# If you just don't know, use normal def

# Note: You can mix def and async def in your path operation functions as much as you need and define each one using
# the best options for you. FastAPI will do the right thing with them. Anyway, in any of the case above, FastAPI will
# still work asynchronously and be extremely fast.

# But by following the steps above, it will be able to do some performance optimizations.


