import matplotlib.pyplot as plt
import numpy as np
from collections.abc import Callable


def graph(
    fn: Callable[[float], float],
    xl: float = 0.01,
    xu: float = 10.0,
    label_x: str = "x-axis",
    label_y: str = "y-axis",
    title: str = "title",
    save_fig: bool = False,
    fig: str = "plot.png",
    show: bool = False,
):
    xp = (xu - xl) / 1000.0
    xpts = np.arange(xl, xu, xp)
    ypts = [fn(x) for x in xpts]

    plt.plot(xpts, ypts)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
    plt.grid(True)

    if save_fig:
        plt.savefig(fig)

    if show:
        plt.show()


def bisection(
    f,
    xl,
    xu,
    es100=0.5,
    imax=1000,
    debug=False,
):
    ea = 1.0  # 100%
    iteration = 0
    x0 = xl
    if debug:
        opers = 0
    while True:
        xr = (xl + xu) / 2.0  # opers = 2
        iteration += 1  # opers = 1
        if xr:
            ea = abs(1 - x0 / xr)  # opers = 3
        if debug:
            opers += 16  # total operations per iteration
            print(
                "iteration={}, xl={:.4f}, xu={:.4f}, xr={:.4f}, ea={:.4%}, opers={}".format(
                    iteration, xl, xu, xr, ea, opers
                )
            )
        test = f(xl) * f(xr)  # opers = 2 + 1 + 2 (count function evaluations twice)
        if test < 0:  # opers = 1
            xu = xr
        elif test > 0:  # opers = 1
            xl = xr
        else:  # test == 0
            ea = 0.0
        if ea * 100 < es100 or iteration >= imax:  # opers = 3
            break
        x0 = xr
    return xr


def falsepos(
    f,
    xl,
    xu,
    es100=0.5,
    imax=1000,
    debug=False,
):
    ea = 1.0  # 100%
    iteration = 0
    x0 = xl
    if debug:
        opers = 0
    while True:
        xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))  # opers = 5
        iteration += 1  # opers = 1
        if xr:
            ea = abs(1 - x0 / xr)  # opers = 3
        if debug:
            opers += 19  # total operations per iteration
            print(
                "iteration={}, xl={:.4f}, xu={:.4f}, xr={:.4f}, ea={:.4%}, opers={}".format(
                    iteration, xl, xu, xr, ea, opers
                )
            )
        test = f(xl) * f(xr)  # opers = 2 + 1 + 2 (count function evaluations twice)
        if test < 0:  # opers = 1
            xu = xr
        elif test > 0:  # opers = 1
            xl = xr
        else:  # test == 0
            ea = 0.0
        if ea * 100 < es100 or iteration >= imax:  # opers = 3
            break
        x0 = xr
    return xr


def fixpt(f, x0, es100=0.5, imax=1000, debug=False):
    xi = float(x0)
    ea = 1.0  # assume 100% relative error to begin
    iteration = 0
    while True:
        xr = f(xi) + xi
        iteration += 1
        if xr:
            ea = abs(1 - xi / xr)
        if debug:
            print(
                "iteration={}, xi={:.8f}, xr={:.8f}, ea={:.2%}".format(
                    iteration, xi, xr, ea
                )
            )
        if ea * 100 < es100 or iteration >= imax:
            break
        xi = xr
    # end while
    return xr


# end fixpt()


def newton(f, df, x0, es100=0.5, imax=1000, debug=False):
    xi = float(x0)
    ea = 1.0  # assume 100% relative error to begin
    iteration = 0
    while True:
        xr = xi - f(xi) / df(xi)
        iteration += 1
        if xr:
            ea = abs(1 - xi / xr)
        if debug:
            print(
                "iteration={}, xi={:.8f}, xr={:.8f}, ea={:.2%}".format(
                    iteration, xi, xr, ea
                )
            )
        if ea * 100 < es100 or iteration >= imax:
            break
        xi = xr
    # end while
    return xr


# end newton()


def secant(f, x0, x1, es100=0.5, imax=1000, debug=False):
    xi, xj = float(x0), float(x1)
    ea = 1.0  # assume 100% relative error to begin
    iteration = 0
    while True:
        xr = xi - f(xi) * (xj - xi) / (f(xj) - f(xi))
        iteration += 1
        if xr:
            ea = abs(1 - xj / xr)
        if debug:
            print(
                "iteration={}, xi={:.8f}, xr={:.8f}, ea={:.2%}".format(
                    iteration, xi, xr, ea
                )
            )
        if ea * 100 < es100 or iteration >= imax:
            break
        xi = xj
        xj = xr
    # end while
    return xr


print("-" * 80)

print("5.3")


# 5.3


def fn_5_3(
    x: float,
) -> float:
    return -26 + (85 * x) + (-91 * (x**2)) + (44 * (x**3)) + (-8 * (x**4)) + (x**5)


## a

print("-" * 80)


print("5.3 a")


# Uncomment one graph call at a time
# graph(
#     fn=fn_5_3,
#     xl=0.555,
#     xu=0.56,
#     save_fig=True,
#     fig="hands_on_module_4.5-3-a.png",
# )


## b

print("-" * 80)

print("5.3 b")


approx_5_3_b = bisection(
    f=fn_5_3,
    xl=0.5,
    xu=1,
    debug=True,
    es100=0.1,
)

print(f"5.3 b bisect approx -> {approx_5_3_b}")

## c

print("-" * 80)

print("5.3 c")

approx_5_3_c = falsepos(
    f=fn_5_3,
    xl=0.5,
    xu=1,
    es100=0.2,
    debug=True,
)

print(f"5.3 c falsepos approx -> {approx_5_3_c}")


print("-" * 80)

print("6.2")


def fn_6_2(
    x: float,
) -> float:
    return (2.1 * (x**3)) + (-11.6 * (x**2)) + (17.5 * x) - 6


def d_fn_6_2(
    x: float,
) -> float:
    return (2.1 * 3 * (x**2)) + (-11.6 * 2 * (x**1)) + 17.5


print("-" * 80)

print("6.2 a")


# Uncomment one graph call at a time
# graph(
#     fn=fn_6_2,
#     xl=3.18,
#     xu=3.2,
#     save_fig=True,
#     fig="hands_on_module_4.6-2-a.png",
# )


print("-" * 80)

print("6.2 b")

approx_6_2_b = fixpt(
    f=fn_6_2,
    x0=3,
    es100=0.1,
    debug=True,
    imax=3,
)

print(f"6.2 b approx -> {approx_6_2_b}")

print("-" * 80)

print("6.2 c")

approx_6_2_c = newton(
    f=fn_6_2,
    df=d_fn_6_2,
    x0=3,
    imax=3,
    debug=True,
)

print(f"6.2 c approx -> {approx_6_2_c}")


print("-" * 80)

print("6.2 d")

approx_6_2_d = secant(
    f=fn_6_2,
    x0=3,
    x1=4,
    imax=3,
    debug=True,
)

print(f"6.2 d approx -> {approx_6_2_d}")

print("-" * 80)
