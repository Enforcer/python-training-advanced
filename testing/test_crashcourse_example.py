import random

import pytest
from pytest_mock.plugin import MockerFixture


@pytest.fixture()
def number() -> int:
    return random.randint(1, 100)


def test_any_name(number: int) -> None:
    assert number > 0


def test_with_mocking(mocker: MockerFixture) -> None:
    random_randint_mock = mocker.patch("random.randint")
    random_randint_mock.return_value = 123

    result = random.randint(0, 10)

    assert result == 123
    random_randint_mock.assert_called_once_with(0, 10)
