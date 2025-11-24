# Write a context manager that will use time.time() function to measure how long it took to execute
# a code under the context manager and will print that information to the screen.
#
# `timeit` should accept a single argument - str that will be printed with duration info.
#
# Make sure `timeit` can be used as both context manager AND decorator.
import time


def timeit():
    pass


@timeit()
def heavy_stuff() -> None:
    time.sleep(0.33)

if __name__ == "__main__":
    with timeit():
        time.sleep(0.3)
        10**1000
        time.sleep(0.2)
    heavy_stuff()

    # You should see printed stats from context manager
    # and decorated function
