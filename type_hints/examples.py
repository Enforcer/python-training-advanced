# typing.reveal_type helps debug types:
#  - if used while running the program, it will tell us actual type
#  - if used during mypy runs, it will tell us what type checker knows
#    without running the code
import random
from typing import reveal_type, Callable

# annotate variables - without value assigned
a: int

# normally, one does not have to do it because of type inference
b = 1 * 2
reveal_type(b)

# but it is considered an error to override variable's type
a = "Hello" + "World"  # a is already declared to be of type 'int'

# Unions - a variable can have one of a few types
c: int | None = 3
reveal_type(c)

# functions
def repeat_string(a_str: str, how_many_times: int) -> str:
    return a_str * how_many_times

result = repeat_string("test", 5)
reveal_type(result)

# kwargs and args - annotation only specifies type of a single argument
def a_function(self, *args: str, **kwargs: int) -> str:
    reveal_type(args)
    reveal_type(kwargs)
    return args[0]


# approach to None
def random_number_or_none() -> int | None:
    number = random.randint(0, 10)
    if number < 5:
        return None
    return number

result = random_number_or_none()
print("Random number * 2 is", result * 2)

# Annotating fields
from typing import ClassVar
from dataclasses import dataclass

@dataclass
class SomeClass:
    class_level_var: ClassVar[int]  # class-level var, 'static variable'
    name: str

SomeClass(name=44)  # considered as an error
SomeClass(name="Sebastian")  # this is fine

# Generics - these are often 'containers' that can contain
# a collection of objects with the same type, they use []
a_list: list[str] = []
a_dict: set[int] = set()

# generic functions
def return_same_thing[T](an_object: T) -> T:
    return an_object

d = return_same_thing(123)
reveal_type(d)
e = return_same_thing(["Sebastian"])
reveal_type(e)

# generic types
class Printer[T]:
    def __init__(self, value: T) -> None:
        self._value = value

    def print(self) -> None:
        print(self._value)

    def get(self) -> T:
        return self._value


printer_ints = Printer[int](1)
reveal_type(printer_ints)
printer_float = Printer(1.0)
reveal_type(printer_float)  # type checker infers type here

# annotating functions as objects
def choose_number_randomly(a_list: list[int]) -> int:
    return random.choice(a_list)

def get_a_number(
    a_list: list[int],
    strategy: Callable[[list[int]], int],
) -> int:
    return strategy(a_list)

# functions with multiple parameters
def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def calc(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)
