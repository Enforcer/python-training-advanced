from secrets import token_hex

class AuthException(Exception):
    pass


class Auth:
    def __init__(self) -> None:
        # keeps mapping of usernames to passwords
        self._users_passwords: dict[str, str] = {}
        # keeps mapping of session ids to usernames
        self._users_sessions: dict[str, str] = {}

    def login(self, username: str, password: str) -> str:
        """Returns a session id in case of successful login."""

        # generate session id if username and password are correct
        # session_id = token_hex()

    def register(self, username: str, password: str) -> None:
        """Creates user account (_users_passwords) if username is unused."""
        pass

    def is_logged_in(self, session_id: str) -> bool:
        """Returns true if given session_id belongs to logged-in user.

        User is logged in if there is an entry in self._users_sessions.
        """
        pass
