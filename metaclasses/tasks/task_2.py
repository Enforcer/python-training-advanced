"""Task - subclasses validation.

Implement GroupMeta so that it validates subclasses of Group class.
It should not validate the Group class itself!

Implement the following rules:
- Each subclass of Group has to have 'name' attribute
- 'name' must be unique across all Group subclasses
- Each subclass of Group has to have parent - either set to another subclass of Group or empty (None)
- Only a single subclass of Group can have parent = None

In case of missing properties, raise exception(s).

You can also remove metaclass altogether and use __init_subclass__ in Group if you prefer.
"""
import unittest


class GroupMeta(type):
    pass


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
