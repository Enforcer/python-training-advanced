# Run mypy in a strict mode on this file:
#   uv run mypy --strict type_hints/task.py
# Fix any issues it reports
# HINT: use reveal_type function to debug what type checker thinks the type is
from typing import reveal_type, Callable
from decimal import Decimal

def divide_integers(a: int, b: int) -> float:
    return a / b

result = divide_integers(10, 5)

names: list[str] = []
while (name := input("Enter your name: ").strip()) != "":
    names.append(name)


def convert_to_decimal(value: int | float) -> Decimal:
    if isinstance(value, int):
        return Decimal(value)
    elif isinstance(value, float):
        return Decimal(str(value))


from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    height: float

person = Person(name="Sebastian", age=18, height=189.5)


def print_var(arg: str) -> None:
    print(arg)


def apply(function: Callable[[str], None], *args: str) -> None:
    for arg in args:
        function(arg)


apply(print_var, "Sebastian", "Python", "Training")
