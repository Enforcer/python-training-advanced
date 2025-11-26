class Example:
    def __init__(self, name: str) -> None:
        self._name = name
        self.__name = name  # name mangling


class Another(Example):
    def __init__(self, name):
        super().__init__(name)
        # name will also be changed and won't collide with Example.__name
        self.__name = name + "Another"


example = Example("Sebastian")
print(example._name)  # you can read it, but you're not supposed to!
print(example._Example__name)  # __name was changed _<class name>__name
print(example.__name)
