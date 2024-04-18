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


# Technical Details

# Modern version of Python have support for "asynchronous code"
# using something called "coroutines" with async and await syntax.

# Let's see that phrase by parts in the sections below:
# *Asynchronous Code
# *async and await
# *Coroutines

# Asynchronous Code

# Asynchronous code just means that the language has a way to tell the computer/program that at some point in the code,
# it will have to wait for something else to finish somewhere else.

# As the execution time is consumed mostly by waiting for I\O operations, they call them "I\O bound" operations
# It's called "asynchronous" because the computer/program doesn't have to be "synchronized" with the slow task, waiting
# for the exact moment that the task finishes, while doing nothing, to be able to take the task result and continue the work

# For "synchronous" (contrary to "asynchronous") they commonly also use the term "sequential",
# because the computer / program follows all the steps in sequence before switching to a different task,
# even if those steps involve waiting.

# Concurrency and Burgers
# This idea of asynchronous code described above is also sometimes called "concurrency". It is different from "parallelism"
# Concurrency and parallelism both relate to "different things happening more or less at the same time".

# But the details between concurrency and parallelism are quite different.
# To see the difference, imagine the following story about burgers:

# Concurrent Burgers
# You go with your crush to get fast food, you stand in line while the cashier takes
# the orders from the people in front of you.

# Then it's your turn, you place your order of 2 very fancy burgers for your crush and you.
# The cashier says something to the cook in the kitchen so they know they have to prepare your burgers
# (even though they are currently preparing the ones for the previous clients).
# You pay.

# The cashier gives you the number of your turn.
# While you are waiting, you go with your crush and pick a table, you sit and talk with your crush for a long time
# (as your burgers are very fancy and take some time to prepare).
