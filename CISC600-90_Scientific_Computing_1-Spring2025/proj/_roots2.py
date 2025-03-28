'''
module: _roots2.py
author: Luis Paris
description:
- implements open methods:
  * fixed-point method
  * newton-raphson method
  * secant method
- comparison rubrics:
  * number of iterations
'''

def fixpt(f, x0, es100=.5, imax=1000, debug=False):
    xi = float(x0)
    ea = 1.  #assume 100% relative error to begin
    iter = 0
    while True:
        xr = f(xi) + xi
        iter += 1
        if xr: ea = abs(1 - xi/xr)
        if debug:
            print('iter={}, xi={:.8f}, xr={:.8f}, ea={:.2%}'
                  .format(iter, xi, xr, ea))
        if ea*100 < es100 or iter >= imax:
            break
        xi = xr
    #end while
    return xr
#end fixpt()

def newton(f, df, x0, es100=.5, imax=1000, debug=False):
    xi = float(x0)
    ea = 1.  #assume 100% relative error to begin
    iter = 0
    while True:
        xr = xi - f(xi) / df(xi)
        iter += 1
        if xr: ea = abs(1 - xi/xr)
        if debug:
            print('iter={}, xi={:.8f}, xr={:.8f}, ea={:.2%}'
                  .format(iter, xi, xr, ea))
        if ea*100 < es100 or iter >= imax:
            break
        xi = xr
    #end while
    return xr
#end newton()

def secant(f, x0, x1, es100=.5, imax=1000, debug=False):
    xi,xj = float(x0),float(x1)
    ea = 1.  #assume 100% relative error to begin
    iter = 0
    while True:
        xr = xi - f(xi)*(xj - xi) / (f(xj) - f(xi))
        iter += 1
        if xr: ea = abs(1 - xj/xr)
        if debug:
            print('iter={}, xi={:.8f}, xr={:.8f}, ea={:.2%}'
                  .format(iter, xi, xr, ea))
        if ea*100 < es100 or iter >= imax:
            break
        xi = xj
        xj = xr
    #end while
    return xr
#end secant()
