"""Task - subclasses registration by name.

Save all classes using RegisteredClass as a metaclass inside it.
Implement get_by_auth_type and get_by_auth_method so they return a list
of matching classes.

You can also use inheritance and __init_subclass__ if you prefer.

*In case of missing properties, exceptions can be silenced.
**Add a test for this case.
"""
import unittest
from collections import defaultdict
from typing import Any


class RegisteredClass(type):
    _by_auth_type: dict[str, list[type]] = defaultdict(list)
    _by_auth_method: dict[str, list[type]] = defaultdict(list)

    def __new__(
        mcls,
        name: str,
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        /,
        **kwargs: Any,
    ) -> type:
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        mcls._by_auth_type[getattr(cls, "auth_type")].append(cls)
        mcls._by_auth_method[getattr(cls, "auth_method")].append(cls)
        return cls

    @classmethod
    def get_by_auth_type(cls, auth_type: str) -> list[type]:
        return cls._by_auth_type[auth_type]

    @classmethod
    def get_by_auth_method(cls, auth_method: str) -> list[type]:
        return cls._by_auth_method[auth_method]


class BasicAuth(metaclass=RegisteredClass):
    auth_type = "basic"
    auth_method = "basic"


class JwtAuth(metaclass=RegisteredClass):
    auth_type = "jwt"
    auth_method = "authorization header"


class OAuth(metaclass=RegisteredClass):
    auth_type = "oath"
    auth_method = "authorization header"


class MetaclassesTask1(unittest.TestCase):
    def test_get_by_auth_type_basic_returns_basic_auth(self) -> None:
        classes = RegisteredClass.get_by_auth_type("basic")

        self.assertEqual(classes, [BasicAuth])

    def test_get_by_auth_method_auth_header_returns_jwt_and_oauth(self) -> None:
        classes = RegisteredClass.get_by_auth_method("authorization header")

        self.assertEqual(2, len(classes))
        self.assertIn(JwtAuth, classes)
        self.assertIn(OAuth, classes)

        
if __name__ == "__main__":
    unittest.main()
