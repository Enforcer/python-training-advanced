from unittest.mock import Mock


mock = Mock()

# Mock can be called...
mock()
# <Mock name='mock()' id='4465157056'>

# Mock's attributes can be generated on-the-fly
mock.method()
# <Mock name='mock.method()' id='4465158064'>
mock.attribute
# <Mock name='mock.attribute' id='4465158400'>

# Mock can be taught what to return
# or they can have 'normal' attributes set
mock.return_value = 44
mock()
# 44

mock.attribute = 123
mock.attribute  # 123

# ...or if they should raise an exception
mock.side_effect = ValueError("WUT")
try:
    mock()
except ValueError as exc:
    print(exc)
    # WUT

# more advanced scenario
# return value, raise exception, then return value
# ...all with list in side_effect
mock = Mock()

mock.side_effect = [1, ValueError("WUT"), 2]
mock()  # 1
mock()  # ValueError
mock()  # 5


# assign custom function to mock
mock = Mock()
mock.method = lambda a: a**2
mock.method(4)  # 16

# mocks can be nested
mock.method.return_value = 555
mock.method()  # 555

# mocks can be interrogated about their interactions
mock = Mock()
mock(name="Sebastian")
mock()
mock.a_method(123)
mock.mock_calls
# [call(name='Sebastian'), call(), call.a_method(123)]

# finally, we can make assertions on mocks

# called exactly once, regardless of arguments
mock.assert_called_once()

# called exactly once, with specific arguments
mock(name="Sebastian")
mock.assert_called_once_with(name="Sebastian")  # ok
mock.assert_called_once_with("Sebastian")  # will fail
# AssertionError: expected call not found.
# Expected: mock('Sebastian')
#   Actual: mock(name='Sebastian')

# assertions on mocks part 2
mock.assert_not_called()  # no calls at all
mock.assert_called()  # no calls at all

from unittest.mock import call

expected_call = call(name="Sebastian")
mock.assert_has_calls([expected_call])

# Simply, how many times mock was called
len(mock.mock_calls)

# mocks can be sealed
from unittest.mock import seal, Mock

mock = Mock()
mock.method.return_value = 123
seal(mock)

mock.method()  # 123
mock.attribute  # AttributeError
mock.method3.return_value = 321  # AttributeError

# mocks can (and should) be configured with spec_set
class Example:
    def foo(self) -> None:
        pass

mock_wo_spec_set = Mock()
mock_with_spec_set = Mock(spec_set=Example)

mock_wo_spec_set.bar()
# <Mock name='mock.bar()' id='4436503792'>

mock_with_spec_set.bar()  # AttributeError
mock_with_spec_set.foo()
# <Mock name='mock.foo()' id='4436504464'>
