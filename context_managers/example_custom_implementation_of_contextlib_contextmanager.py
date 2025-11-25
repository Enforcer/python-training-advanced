
# rough, incomplete equivalent of contextlib.contextmanager
def my_context_manager(fun):
    class ContextManager:
        def __init__(self, *args, **kwargs):
            self._generator = fun(*args, **kwargs)

        def __enter__(self) -> None:
            next(self._generator)  # proceed to yield

        def __exit__(self, exc, exc_type, tb) -> None:
            try:
                next(self._generator)
            except StopIteration:
                pass # all good
            else:
                raise RuntimeError("Generator should stop!")

    return ContextManager


@my_context_manager
def fun(a):
    print("Before yield")
    print(a)
    yield
    print("After yield")


with fun(1):
    print("Start")
    print("Stop")
