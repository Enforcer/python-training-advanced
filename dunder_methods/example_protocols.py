from typing import Iterable, Iterator, Self

class Example:  # Iterable
    def __iter__(self) -> Iterator[int]:
        return ...


print(isinstance(Example(), Iterable))


class ExampleIterator:
    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        return 1  # or raise StopIteration to stop


print(isinstance(ExampleIterator(), Iterator))
print(isinstance(ExampleIterator(), Iterable))