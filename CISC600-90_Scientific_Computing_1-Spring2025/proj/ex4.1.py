import series


def fn(
    x: float,
    i: int,
) -> float:
    """Example polynomial that gives the _i_th derivate of the function evaluated at _x_

    Args:
        x (float): evaluated at _x_
        i (int): _i_th order derivate

    Returns:
        float: true value
    """
    return {
        # 0th order derivative, essentially the original f(x)
        0: -0.1 * x**4 - 0.15 * x**3 - 0.5 * x**2 - 0.25 * x + 1.2,
        1: -0.4 * x**3 - 0.45 * x**2 - x - 0.25,
        2: -1.2 * x**2 - 0.9 * x - 1,
        3: -2.4 * x - 0.9,
        4: -2.4,
    }.get(i, 0)


x = 0
h = 1

print(f"Actuat value for {x=}: {fn(x, 0)}")
print(f"Actuat value for {x+1=}: {fn(x+1, 0)}")

for i in range(0, 10):
    print(f"Taylor Approximation with {i=}: {series.taylor(fn, i, x, 1)}")
