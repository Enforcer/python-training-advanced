# Write a function that will be caching results for two given arguments.
# Use a dict as cache storage.
# First, check if a given combination of arguments is in cache.
#   If not, calculate it using function decorated, store results in cache and then return
#   If the result is in cache, then return it from cache
#
# The result should be that if you call add(1, 2) twice, you will see "Adding 1 and 2" only once


def cache(fun):
    return fun


@cache
def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b


add(1, 2)
add(1, 2)
print("You should see 'Adding 1 and 2' only once")
