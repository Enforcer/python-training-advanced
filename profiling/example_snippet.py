import time
from enum import StrEnum


class State(StrEnum):
    OK = "ok"
    ERROR = "error"
    FAIL = "fail"


class Foo:
    def __init__(self) -> None:
        self._state_changed_at = None
        self._old_state = None
        self._state = None

    def bar(self, state: str) -> None:
        is_valid_state = state in State
        if is_valid_state:
            now = time.time()
            self._state_changed_at = now
            self._old_state = self._state
            self._state = state