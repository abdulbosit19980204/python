# Run the code

# All the code blocks can be copied and used directly (they are actually tested Python files).
# To run any of the examples, copy the code to a file main.py and start uvicorn with:

"""
uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.


"""
# Install FastAPI

# The first step is to install FastAPI.
# For the tutorial, you might want to install it with all the optional dependencies and features:

# pip install "fastapi[all]"
# ... that also includes uvicorn, that you can use as the server that runs your code

