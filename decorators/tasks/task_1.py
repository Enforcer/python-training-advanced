# Built-in function time.time() returns current time in float.
# Use it and decorator to count how long an execution of a function.
# Example for measuing time:
#   start = time.time()
#   ...  # (processing)
#   end = time.time()
#   duration = end - start
#
# Print the result

import time

def timer(fun):
    pass


@timer
def long_function():
    time.sleep(1.3)
