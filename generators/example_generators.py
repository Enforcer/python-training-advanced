# Infinite generator
from typing import Iterator


def count() -> Iterator[int]:
    number = 1
    while True:
      yield number
      number += 1


for number in count():
    if number == 5:
        break
    print(number)


# yield behaviour
def verbose_count() -> Iterator[int]:
    print("Starting")
    number = 1
    print("Before loop")
    while True:
        print("before yield")
        yield number
        print("after yield")
        number += 1

gen = verbose_count()
print(gen)  # <generator object verbose_count at 0x100fab920>
# no other prints
print(next(gen))
# Starting
# Before loop
# before yield
# 1
print(next(gen))
# next(gen)
# after yield
# before yield
# 2


# Built-in generator
for number in range(3):
    print(number)  # 0 1 2


# Reimplementation of range
from typing import Iterator


def numbers_up_to(upper_bound: int) -> Iterator[int]:
  number = 0
  while number < upper_bound:
    yield number
    number += 1


for number in numbers_up_to(3):
  print(number)


# Infinite generator - Fibonacci sequence
def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


import itertools

# Gets first 10 elements - most concise way
for element in itertools.islice(fibonacci(), 10):
    print(element)


# Using enumerate
for index, element in enumerate(fibonacci()):
    print(index, element)
    if index > 10:
        break

# Using zip function with range to limit the number of iterated elements to 10
print(list(zip([1, 2], [4, 5, 6])))
for index, element in zip(range(10), fibonacci()):
    print(element)

from itertools import batched


collection = list(range(10_000))

i = 0
for batch in batched(collection, 10):
    print(batch)

    i += 1
    if i > 10:
        break