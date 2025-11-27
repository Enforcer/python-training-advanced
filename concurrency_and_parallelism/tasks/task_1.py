"""
There is a given list of URLs to be visited and their status code checked.

Choose the right Executor subclass (Thread, Process or Subinterpreter),
so that it uses the least number of resources and allows to process URLs getting
in parallel.

Run the Executor in a context manager, send all urls to check.

For verification, print results of all futures.
You should see numbers 200, 201, 204, 400, 500 and 504 - in random order.

Use between 2-4 workers and observe the speed-up.
"""
import concurrent.futures

import httpx


def get_url_status_code(url: str) -> int:
    response = httpx.get(url)
    return response.status_code


URLS = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/201"
    "https://httpbin.org/status/204",
    "https://httpbin.org/status/400"
    "https://httpbin.org/status/500"
    "https://httpbin.org/status/504"
]
