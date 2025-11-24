# finish implementation of a decorator factory `requires_role`
# It should return a decorator that will check if role passed as keyword argument
# to the function is equal to the one configured.
# If the role is ok, then proceed with the function.
# If the role is different than expected or not present in kwargs, then return "PERMISSION_DENIED" string.
#
# For example,
# @requires_role('admin')
# def foo(a, b, **kwargs):
#     return a + b
#
# foo(1, 2, 'admin')  # OK, 3
# foo(1, 2, 'user')  # NOT OK, "PERMISSION_DENIED"
# foo(1, 2)  # NOT OK, "PERMISSION_DENIED"
#

def requires_role(role):
    def decorator(fun):
        return fun
    return decorator


@requires_role('admin')
def foo(a, b, **kwargs):
    return a + b


assert foo(1, 2, role='admin') == 3
assert foo(1, 2, role='user') == "PERMISSION_DENIED"
assert foo(1, 2) == "PERMISSION_DENIED"
print("OK")
