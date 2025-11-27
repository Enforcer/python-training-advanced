import builtins
from unittest import TestCase
from unittest.mock import Mock, patch


def my_function(filename):
    f = open(filename, "w")
    f.write("gibberish")
    f.close()


class Task4(TestCase):
    def test_patching(self):
        """
        Patch 'open' function from 'builtins' module with patch.object.

        Use "open_mock" as a new value for builtins.open.

        Test should be passing and no file "test_patching_easy.file"
        should be created if you succeeded.
        """
        opened_file_mock = Mock()
        open_mock = Mock(return_value=opened_file_mock)

        my_function("test_patching_easy.file")

        opened_file_mock.write.assert_called_once_with("gibberish")
        opened_file_mock.close.assert_called_once_with()
