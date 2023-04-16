from rply.token import BaseBox


class NumBox(BaseBox):
    def __init__(self, value: int):
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value
