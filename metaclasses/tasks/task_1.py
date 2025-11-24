"""Task - subclasses registration by name.

Save all classes using RegisteredClass as a metaclass inside it.
Implement get_by_auth_type and get_by_auth_method so they return a list
of matching classes.

You can also use inheritance and __init_subclass__ if you prefer.

*In case of missing properties, exceptions can be silenced.
**Add a test for this case.
"""
import unittest


class RegisteredClass(type):
    pass

    @classmethod
    def get_by_auth_type(cls, auth_type: str) -> list[type]:
        return []

    @classmethod
    def get_by_auth_method(cls, auth_method: str) -> list[type]:
        return []


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
