from math import cos, pi, sin
import series


def fn(
    x: float,
    n: int,
) -> float:
    """function cos(x) evaluated at _x_ for the _n_th derivative

    Args:
        x (float): evaluation point
        n (int): derivative

    Returns:
        float: value
    """
    return {
        0: cos(x),
        1: -sin(x),
        2: -cos(x),
        3: sin(x),
    }.get(n % 4)


x = pi / 4.0
h = pi / 12.0

print(f"Actuat value for {x=}: {fn(x, 0)}")
print(f"Actuat value for x={pi/3.0}: {fn(pi/3.0, 0)}")

for i in range(0, 10):
    print(f"Taylor Approximation with {i=}: {series.taylor(fn, i, x, h)}")
