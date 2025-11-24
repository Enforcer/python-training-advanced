from collections.abc import Callable

def printing_decorator[**P, T](func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwds: P.kwargs) -> T:
        print("Calling", func)
        return func(*args, **kwds)
    return wrapper


@printing_decorator
def add(a: int, b: int) -> int:
    return a + b


reveal_type(add(1, 2))


# Decorators factory - basic example
def decorator_factory[F: Callable[..., Any]](arg: int) -> Callable[[F], F]:
    def empty_wrapper(func):
        return func
    return empty_wrapper


# Typed decorators factories
from typing import Any, Callable
from functools import wraps


def multiply_result[F: Callable[..., Any]](how_many_times: int) -> Callable[[F], F]:
    def _multiply_result(fun):
        @wraps(fun)
        def new_fun(*args, **kwargs):
            result = fun(*args, **kwargs)
            return result * how_many_times
        return new_fun
    return _multiply_result


@multiply_result(3)
def add_to_decorate_with_factory(a: int, b: int) -> int:
    return a + b

reveal_type(add_to_decorate_with_factory(1, 2))