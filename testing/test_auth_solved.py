import pytest
from auth_solved import Auth, UsernameTaken


def test_registering_user_with_new_username_and_password_returns_none() -> None:
    auth = Auth()

    response = auth.register(username="Seba", password="secret1")

    assert response is None


def test_login_to_existing_account_returns_session_token() -> None:
    auth = Auth()
    auth.register(username="Seba", password="secret1")

    session_token = auth.login(username="Seba", password="secret1")

    assert isinstance(session_token, str) and len(session_token) > 0

def test_registration_using_taken_username_raises_exception() -> None:
    auth = Auth()
    auth.register(username="Seba", password="secret1")

    with pytest.raises(UsernameTaken):
        auth.register(username="Seba", password="secret2")

def test_valid_session_token_of_logged_in_user_returns_username() -> None:
    auth = Auth()
    auth.register(username="Seba", password="secret1")
    session_token = auth.login(username="Seba", password="secret1")

    username = auth.is_logged_in(session_token)

    assert username == "Seba"
