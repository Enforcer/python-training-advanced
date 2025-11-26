from secrets import token_hex

class AuthException(Exception):
    pass


class UsernameTaken(AuthException):
    pass


class Auth:
    def __init__(self) -> None:
        # keeps mapping of usernames to passwords
        self._users_passwords: dict[str, str] = {}
        # keeps mapping of session ids to usernames
        self._users_sessions: dict[str, str] = {}

    def login(self, username: str, password: str) -> str:
        """Returns a session id in case of successful login."""

        if self._users_passwords.get(username) == password:
            # generate session id if username and password are correct
            session_token = token_hex()
            self._users_sessions[session_token] = username
            return session_token

    def register(self, username: str, password: str) -> None:
        """Creates user account (_users_passwords) if username is unused."""
        if username in self._users_passwords:
            raise UsernameTaken
        self._users_passwords[username] = password

    def is_logged_in(self, session_id: str) -> str | None:
        """Returns true if given session_id belongs to logged-in user.

        User is logged in if there is an entry in self._users_sessions.
        """
        if session_id in self._users_sessions:
            return self._users_sessions.get(session_id)
