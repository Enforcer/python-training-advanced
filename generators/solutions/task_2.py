# Write an infinite generator function called even_numbers() that starts at 0 and yields the next even number on each call (0, 2, 4...)
#
# Use a for loop with a break statement to print the first ten even numbers generated.
from itertools import islice

print("Solution with range")
limit = 10 * 2
for number in range(0, limit, 2):
    print(number)


print("Solution with generator function")
def generate_even():
    number = 0
    while True:
        yield number
        number += 2



