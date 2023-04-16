from ctypes import cdll
from ctypes import c_int


name = "./src/Begemot/components/minus.so"
library = cdll.LoadLibrary(name)


def minus(a: int, b: int) -> int:
    return int(library.minus(c_int(a), c_int(b)))
