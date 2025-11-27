from unittest import TestCase
from unittest.mock import Mock


class Task3(TestCase):
    def test_retrying_function_retries_after_one_exception(self):
        """Finish the test implementation by:
        - set side_effect on mock so that for the first time it
          raises exception and only on the second attempt it returns value "55"
        - write assertion that mock was called twice
        """
        mock = Mock()

        result = retrying_function(mock)

        self.assertEqual(55, result)

    def test_it_tries_up_to_3_times_then_reraises_exception(self):
        """Implement a scenario with a mock that only returns exception.
        retrying function SHOULD retry 3 times, then reraise the exception.

        Write assertions:
        - retrying function raises exception
        - mock was called 3 times
        """



def retrying_function(mock: Mock) -> None:
    last_exc = None
    for _ in range(3):
        try:
            last_exc = None
            result = mock()
        except Exception as exc:
            print("oh no")
            last_exc = exc
        else:
            return result
    if last_exc is not None:
        raise last_exc
