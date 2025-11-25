# Built-in function time.time() returns current time in float.
# Use it and decorator to count how long an execution of a function.
# Example for measuing time:
#   start = time.time()
#   ...  # (processing)
#   end = time.time()
#   duration = end - start
#
# Print the result
from functools import wraps
import time

def timer(fun):
    @wraps(fun)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        duration = time.time() - start
        print(f"{fun} took {duration}s")
        return result
    return wrapped


@timer
def long_function():
    time.sleep(1.3)


long_function()
