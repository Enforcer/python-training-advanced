import sys
from unittest.mock import patch

with patch("sys.setswitchinterval") as setswitchinterval_mock:
    print(sys.setswitchinterval)
    print(sys.setswitchinterval is setswitchinterval_mock)
    # True

# After patch context-manager
print(sys.setswitchinterval is setswitchinterval_mock)
# False

class Foo:
    def bar(self) -> None:
        pass

foo = Foo()

with patch.object(foo, "bar") as bar_mock:
    print(foo.bar)
    print(foo.bar is bar_mock)  # True

print(foo.bar is bar_mock)  # False


# When patching, one can pass the configured mock
from unittest.mock import Mock


mock = Mock(side_effect=ValueError("Example"))
with patch("sys.setswitchinterval", mock) as setswitchinterval_mock:
    print(setswitchinterval_mock is mock)  # True


# ...or any other object
def substitute(arg):
    raise ValueError(f"{arg} is too big!")

with patch("sys.setswitchinterval", substitute) as setswitchinterval_mock:
    print(setswitchinterval_mock is substitute)  # True
    sys.setswitchinterval(3)  # raises ValueError("3 is too big!")
