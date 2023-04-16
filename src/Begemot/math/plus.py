from ctypes import cdll
from ctypes import c_int


name = "./src/Begemot/components/plus.so"
library = cdll.LoadLibrary(name)


def plus(a: int, b: int) -> int:
    return int(library.plus(c_int(a), c_int(b)))
