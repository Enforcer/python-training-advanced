from typing import Self


class Example:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Example({self.value})"

    def __add__(self, other: Self) -> Self:
        return Example(self.value + other.value)

    def __sub__(self, other) -> Self: ...  # -
    def __mul__(self, other) -> Self: ... # *
    def __pow__(self, other) -> Self: ... # **
    def __truediv__(self, other): ...  # /
    def __floordiv__(self, other): ...  # //


print(Example(1) + Example(4))


# Exceptions
# |_ ArithmeticError
#  |_ FloatingPointError
#  |_ OverflowError
#  |_ ZeroDivisionError
