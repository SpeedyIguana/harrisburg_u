"""
module: _roots_opers.py
author: Luis Paris
description:
- implements bracketing methods:
  * bisection
  * false position
- comparison rubrics:
  * number of iterations
  * number of operations (new!)
"""


def bisect(f, xl, xu, es100=0.5, imax=1000, debug=False):
    xl, xu = float(xl), float(xu)
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


def falsepos(f, xl, xu, es100=0.5, imax=1000, debug=False):
    xl, xu = float(xl), float(xu)
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
