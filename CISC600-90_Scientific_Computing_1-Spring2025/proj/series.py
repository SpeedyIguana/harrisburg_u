from collections.abc import Callable
from math import factorial


def taylor(fn: Callable[[float, int], float], n: int, x: int, h: int):
    return 0 if n < 0 else ((fn(x, n) / factorial(n)) * h**n) + taylor(fn, n - 1, x, h)
