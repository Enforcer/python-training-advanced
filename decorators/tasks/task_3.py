# Write a decorator that will ensure that all passed arguments are integers.
# If any argument is not an integer, then return 0.
# To check if a given thing is an integer, you can do `isinstance(thing, int)`


def only_integers_accepted(fun):
    return fun


@only_integers_accepted
def a_function(a, *args, **kwargs):
    print(f"Got {a}, {args} and {kwargs}")
    return a + sum(args) + sum(kwargs.values())


result = a_function(1, 2, 3, **{"d": 1})
assert result == 7
result_2 = a_function(10_000, **{"name": "Sebastian"})
assert result_2 == 0
