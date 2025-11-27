from unittest import TestCase
from unittest.mock import Mock


class Client:
    def save_data(self, data: list[int]) -> None:
        pass


class Handler:
    def __init__(self, client: Client) -> None:
        self._client = client

    def handle(self, *args: int) -> None:
        data = [n**2 for n in args]
        self._client.save_dat(data)


class Task2(TestCase):
    def test_passing(self):
        """This test is passing but it should not.

        Make sure mock ACCURATELY mimics Client class - use spec_set.

        First, secure the mock, then fix the test
        and finally the code of Handler class.

        Also, seal the mock after you configured it.
        """
        mock = Mock()
        handler = Handler(mock)

        handler.handle(1, 2)

        mock.save_dat.assert_called_once_with([1, 4])
