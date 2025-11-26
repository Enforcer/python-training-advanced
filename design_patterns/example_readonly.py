class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    # read-only 'field'
    @property
    def name(self) -> str:
        return self._name


person = Person("Sebastian")
print(person.name)
person.name = "Michał"  # error
person._name  # tools warn you this is private
