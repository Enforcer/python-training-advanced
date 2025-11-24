# Example

with open("multi_line_file", "w") as f:  # <-- context manager
    pass


# Basic definition
from types import TracebackType


class ContextManager:
    def __init__(self) -> None:
        print("__init__")

    # context manager protocol
    def __enter__(self) -> None:
        print("Entering")

    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException | None,
        exc_traceback: TracebackType | None,
    ) -> bool | None:  # True if it should suppress exception
        print("Exiting")

    # end of context manager protocol


with ContextManager():
    print("Inside")

# __init__
# Entering
# Inside
# Exiting

# Modern approach with functions
from contextlib import contextmanager
from typing import Iterator, reveal_type


@contextmanager
def context_manager() -> Iterator[None]:
    print("Entering")
    yield
    print("Existing")


with context_manager():
    print("Inside")

# Entering
# Inside
# Existing

# Function-based context manager can accept
# arguments and make them available using yield
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def context_manager_with_arguments(arg: int) -> Iterator[str]:
    print("Entering")
    yield "text" * arg
    print("Existing")


with context_manager_with_arguments(3) as text:
    print("Inside", f"text: {text}")


# context decorator
@context_manager_with_arguments(3)
def fun_cm_function():
    return "text"


fun_cm_function()


# ContextDecorator - context manager that can be used
# also as a function decorator
from contextlib import ContextDecorator
from types import TracebackType


class print_calls(ContextDecorator):
    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self) -> None:
        print(f"Before - {self.name}")

    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException | None,
        exc_traceback: TracebackType | None,
    ) -> bool | None:
        print(f"After - {self.name}")


with print_calls(name="Foo"):
    print("Inside context manager")


@print_calls(name="Bar")
def fun() -> None:
    print("Inside fun")


fun()


# Using multiple context managers at once
from contextlib import suppress  # will silence a specific exception


with (
    suppress(ZeroDivisionError),
    suppress(ValueError),
    suppress(TypeError),
):
    pass  # nasty code it must be

# Variable number of context managers to open - ExitStack
# Source: https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack
from contextlib import ExitStack


file_names = ["multi_line_file", "single_line_file"]
with ExitStack() as stack:
    files = [stack.enter_context(open(name)) for name in file_names]
    # open and close variable number of files using
    # single context manager


# When we have optional use of context manager,
# nullcontext might come in handy
#
#     cm = optional_cm if condition else nullcontext()
#     with cm:
#         ...
#
from contextlib import nullcontext

with nullcontext():
    ...


# Typing
from contextlib import contextmanager, AbstractContextManager


@contextmanager
def empty_cm() -> Iterator[None]:
    yield


# no value returned
cm: AbstractContextManager[None] = empty_cm()


@contextmanager
def empty_cm_returning_int() -> Iterator[int]:
    yield 1


cm2: AbstractContextManager[int] = empty_cm_returning_int()

# NOTE: Iterator[X] is equivalent to Generator[X, None, None]
