class GameCell:
    def __init__(self, value: int):
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
