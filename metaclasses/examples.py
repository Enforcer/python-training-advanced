from typing import Any


class Example:
    pass


instance = Example()


type_of_instance = type(instance)
print(type_of_instance)  # Example

type_of_example = type(Example)
print(type_of_example)  # type

print(isinstance(Example, type))

# Just like we create instances from a class,
# classes are created from a metaclass

# Same thing
class ExampleInheritance(Example):
    attr = 100

print(ExampleInheritance.__dict__)

ExampleInheritance = type("ExampleInheritance", (Example,), {"attr": 100})

print(ExampleInheritance.__dict__)


class MyMetaClass(type):
    def __new__(
        mcls,
        name: str,
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        /,
        **kwargs: Any,
    ) -> type:
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        return cls

class AnotherExample(metaclass=MyMetaClass):
    def foo(self) -> None:
        pass

# AnotherExample()


class BaseCls:
    @classmethod
    def __init_subclass__(cls, **kwargs: dict[str, Any]) -> None:
        # inheriting class already exists at this stage
        print(cls)


class InheritingCls(BaseCls, name="Sebastian"):
    pass
