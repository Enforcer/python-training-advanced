from unittest import TestCase
from unittest.mock import Mock


class Task1(TestCase):
    def test_basic_mock_return_value(self):
        """Create an instance of Mock.

        "Teach it" to return 40 when it is called.
        Pass it to the function "calculate" so
        it can use the mock and this test passes.
        """
        mock = ...

        result = calculate(mock)

        self.assertEqual(80, result)

    def test_basic_mock_raises_exception(self):
        """Create an instance of Mock.

        "Teach it" to raise ValueError when it's called.

        Pass it to the function "calculate" so
        it can use the mock and this test passes.
        """
        mock = ...

        result = calculate(mock)

        self.assertEqual(-1, result)


def calculate(mock: Mock):
    try:
        return mock() * 2
    except ValueError:
        return -1
