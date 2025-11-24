from concurrent.futures import Future

future = Future()
future.done()  # False

future.result(timeout=1.0)  # raises TimeoutError after 1s
future.set_result(123)  # mark future as done and set result
# Optionally, you can set exception - future.set_exception
future.result()  # if done, returns result immediately. If not, waits