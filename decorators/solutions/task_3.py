# Write a decorator that will ensure that all passed arguments are integers.
# If any argument is not an integer, then return 0.
# To check if a given thing is an integer, you can do `isinstance(thing, int)`
from functools import wraps


def only_integers_accepted(fun):
    @wraps(fun)
    def wrapped(*args, **kwargs):
        all_arguments = args + tuple(kwargs.values())
        for arg in all_arguments:
            if not isinstance(arg, int):
                print(f"Not an integer detected! {arg}")
                return 0

        return fun(*args, **kwargs)
    return wrapped


@only_integers_accepted
def a_function(a, *args, **kwargs):
    print(f"Got {a}, {args} and {kwargs}")
    return a + sum(args) + sum(kwargs.values())


result = a_function(1, 2, 3, **{"d": 1})
assert result == 7
result_2 = a_function(10_000, **{"name": "Sebastian"})
assert result_2 == 0
