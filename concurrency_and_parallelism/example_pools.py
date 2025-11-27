# threads
def threads() -> None:
    from concurrent.futures import ThreadPoolExecutor

    import httpx


    futures = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        future = executor.submit(httpx.get, "http://example.com")
        futures.append(future)

    print([future.result().status_code for future in futures])

# processes
def processes() -> None:
    from concurrent.futures import ProcessPoolExecutor

    import httpx


    futures = []
    with ProcessPoolExecutor(max_workers=2) as executor:
        future = executor.submit(httpx.get, "http://example.com")
        futures.append(future)

    print([future.result().status_code for future in futures])


def subinterpreters() -> None:
    from concurrent.futures import InterpreterPoolExecutor

    import httpx

    futures = []
    with InterpreterPoolExecutor(max_workers=2) as executor:
        future = executor.submit(httpx.get, "http://example.com")
        futures.append(future)

    print([future.result().status_code for future in futures])

if __name__ == "__main__":
    threads()
    processes()
    try:
        subinterpreters()
    except ImportError:
        print("WARNING: Your python version does not support subinterpreters, start from Python 3.14")
