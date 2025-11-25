import pytest
from auth import Auth


def test_login_to_non_existing_account_raises_exception() -> None:
    auth = Auth()
    pytest.fail("Not implemented")


def test_login_to_existing_account_returns_session_id() -> None:
    pytest.fail("Not implemented")
