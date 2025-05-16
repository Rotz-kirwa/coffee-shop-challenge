class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = name

    @property
    def name(self):
        return self._name

    # Make name immutable by not providing a setter
