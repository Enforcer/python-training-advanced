# mypy: disable-error-code="no-redef"
def decorator(fun_or_cls):
    print(f"Decorating {fun_or_cls}")
    return fun_or_cls


@decorator
class Example:
    @decorator
    def __init__(self, name: str) -> None:
        self.name = name


@decorator
def fun():
    pass


# '@' is just a syntactic sugar
def another_fun(a, b):
    pass

another_fun = decorator(another_fun)

# is equivalent to

@decorator
def another_fun(a, b):
    pass


# More complex example
def double_result(fun):
    def new_fun(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result * 2

    return new_fun

@double_result
def add(a, b):
    return a + b

add(1, 2)  # 6
add  # <function double_result.<locals>.new_fun at 0xE>


# Make new function look like the original
from functools import wraps

def double_result_2(fun):
    @wraps(fun)  # < copies name from fun to new_fun
    def new_fun(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result * 2
    return new_fun

@double_result_2
def add(a: int, b: int) -> int:
    return a + b

add  # <function add at 0x107ea1e80>
add.__annotations__  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


# Decorators factories
from functools import wraps

def multiply_result(how_many_times):
    def _multiply_result(fun):
        @wraps(fun)  # < copies name from fun to new_fun
        def new_fun(*args, **kwargs):
            result = fun(*args, **kwargs)
            return result * how_many_times
        return new_fun
    return _multiply_result


@multiply_result(3)
def add(a, b):
    return a + b


# Basic example - with generics!
# Source: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#decorators
from collections.abc import Callable
from typing import Any


def bare_decorator[F: Callable[..., Any]](func: F) -> F:
    return func


# Practical example - decorator without factory
# Based on https://mypy.readthedocs.io/en/stable/generics.html#declaring-decorators
from collections.abc import Callable
from typing import Any, cast


def double_result_no_arguments[**P, T: int](func: Callable[P, T]) -> Callable[P, T]:
    @wraps(fun)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        result = func(*args, **kwargs)
        return cast(T, result * 2)
    return wrapper

@double_result_no_arguments
def add_to_decorate(a: int, b: int) -> int:
    return a + b


reveal_type(add_to_decorate(1, 2))


# Decorators factory - basic example
def decorator_factory[F: Callable[..., Any]](arg: int) -> Callable[[F], F]:
    def empty_wrapper(func):
        return func
    return empty_wrapper


# Typed decorators factories
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
def add(a: int, b: int) -> int:
    return a + b

reveal_type(add(1, 2))