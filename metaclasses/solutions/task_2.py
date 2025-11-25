"""Task - subclasses validation.

Implement GroupMeta so that it validates subclasses of Group class.
It should not validate the Group class itself! (to exclude it, you can check its name).

Implement the following rules:
- Each subclass of Group has to have 'name' attribute
- 'name' must be unique across all Group subclasses
- Each subclass of Group has to have parent - either set to another subclass of Group or empty (None)
- Only a single subclass of Group can have parent = None

In case of missing properties, raise exception(s).

You can also remove metaclass altogether and use __init_subclass__ in Group if you prefer.
"""
import unittest
from typing import Any


class GroupMeta(type):
    _names_to_classes: dict[str, type] = {}
    _root_group: type | None = None

    def __new__(
        mcls,
        name: str,
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        /,
        **kwargs: Any,
    ) -> type:
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        if cls.__name__ == "Group":
            return cls

        if not (name := namespace.get("name")):
            raise Exception("'name' attribute is mandatory")

        if cls_using_name := mcls._names_to_classes.get(name):
            raise Exception(f"Name '{name}' is already taken by {cls_using_name}")

        if (parent := namespace.get("parent")) is None:
            if mcls._root_group is None:
                mcls._root_group = cls
            else:
                raise Exception(f"There already is a root group called {mcls._root_group}")
        elif not issubclass(parent, Group):
            raise Exception("'parent' must be a subclass of Group!")


        mcls._names_to_classes[name] = cls
        return cls


class Group(metaclass=GroupMeta):
    pass


class Company(Group):
    name = "company"
    parent = None


class BusinessUnit(Group):
    name = "business_unit"
    parent = Company


class MetaclassesTask2(unittest.TestCase):
    def test_lack_of_name_raises_exception(self) -> None:
        with self.assertRaises(Exception):
            class Anonymous(Group):
                parent = Company

    def test_duplicated_name_raises_exception(self) -> None:
        with self.assertRaises(Exception):
            class DuplicatedCompany(Group):
                name = "company"

    def test_duplicated_parent_none_raises_exception(self) -> None:
        with self.assertRaises(Exception):
            class CompanyA(Group):
                name = "company_a"
                parent = None

    def test_parent_int_raises_exception(self) -> None:
        with self.assertRaises(Exception):
            class CompanyB(Group):
                name = "company_b"
                parent = int


if __name__ == "__main__":
    unittest.main()
