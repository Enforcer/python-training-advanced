# Run mypy in a strict mode on this file:
#   uv run mypy --strict type_hints/task.py
# Fix any issues it reports
# HINT: use reveal_type function to debug what type checker thinks the type is
from typing import reveal_type
from decimal import Decimal

def divide_integers(a, b):
    return a / b

result = divide_integers(10, 5)

names: list = []
while (name := input("Enter your name: ").strip()) != "":
    names.append(name)


def convert_to_decimal(value):
    if isinstance(value, int):
        return Decimal(value)
    elif isinstance(value, float):
        return Decimal(str(value))


from dataclasses import dataclass

@dataclass
class Person:
    pass

person = Person(name="Sebastian", age=18, height=189.5)


def print_var(arg: str) -> None:
    print(arg)


def apply(function, *args: str):
    for arg in args:
        function(arg)


apply(print_var, "Sebastian", "Python", "Training")
