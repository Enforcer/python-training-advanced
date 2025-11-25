# Write a function countdown(start) that takes an integer as an argument
# and will count down from a given number to 0 by printing numbers.
# If its given a number smaller or equal to 0, return immediately.

def countdown(start):
    if start <= 0:
        return []

    for number in range(start, -1, -1):
        yield number


assert list(countdown(3)) == [3, 2, 1, 0]
assert list(countdown(0)) == []
print("OK")

def countdown(start):
    if start <= 0:
        return []

    number = start
    while number >= 0:
        yield number
        number -= 1

assert list(countdown(3)) == [3, 2, 1, 0]
assert list(countdown(0)) == []
print("OK")
