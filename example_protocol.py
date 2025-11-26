from typing import Protocol, Iterator, runtime_checkable


class Iterable(Protocol):
    def __iter__(self) -> Iterator:
        pass


class ConvertableToStr(Protocol):  # needed for str
    def __str__(self) -> str:
        pass


@runtime_checkable  # required for isinstance to work
class Duck(Protocol):
    def quack(self) -> None:
        pass


class Example:
    def __iter__(self):
        return iter([1, 2, 3])

    def quack(self) -> None:
        pass


instance: Duck = Example()
print(isinstance(instance, Duck))
print(str(Example()))
a_dict = {}
a_dict[[1, 2, 3 ]]