class Example:
    def __new__(cls):  # instance creation
        print(f"{cls} __new__")
        return super().__new__(cls)

    def __init__(self) -> None:  # initialization
        print(f"{self} __init__")

    def __del__(self) -> None:  # finalizing
        print(f"{self} __del__")


example = Example()