# Write a context manager that will first be locking a given resource before it can continue.
# The locking will happen by adding a name of the resource to the set `locked_resources`
# If the resource is already in the set (locked), then just print "Resource {resource} already locked" and continue.
# If the resource is not yet in the set, then print "Locking resource {resource}" and continue
#
# Remember to remove the resource from the set right before context manager finishes!
from contextlib import contextmanager


locked_resources = set()


@contextmanager
def lock_resource(resource):
    yield


with lock_resource("hdd"):  # should print "Locking resource hdd"
    with lock_resource("hdd"):  # should print "Resource hdd already locked"
        pass

    with lock_resource("cpu"):  # should print "Locking cpu resource"
        pass

    with lock_resource("cpu"):  # should print "Locking cpu resource"
        pass
