import math

import numpy as np
from interpolate import newton, lagrange, newton_interpolate, lagrange_interpolate
from functions import func
from nodes import get_czebyshev, get_nodes
from draw import draw_func


def main():
    func = lambda x: math.sin((4 * x) / math.pi) * math.e ** (-0.2 * x / math.pi)
    n = 60
    a = -5
    b = 10

    coordinates = get_czebyshev(func, 20, -5, 10)
    # coordinates = get_nodes(func, n, a, b)
    x = newton_interpolate(coordinates)
    print("Finished interpolating with Newton's method.")
    y = lagrange_interpolate(coordinates)
    print("Finished interpolating with Lagrange's method.")
    print("Drawing plot now...")
    draw_func(1000, -5, 10, True, False, coordinates, x, y, func)
    # def draw_func(n, a, b, plotly=False, sepplots=False, *args):


def errors():
    a = -5
    b = 10
    numpoints = 1000
    func = lambda x: math.sin((4 * x) / math.pi) * math.e ** (-0.2 * x / math.pi)
    for n in range(1, 30):
        coordinates = get_czebyshev(func, n, a, b)
        f = newton_interpolate(func, n, a, b)
        fvalues = [f(i) for i in np.linspace(a, b, num=numpoints)]


if __name__ == '__main__':
    main()
    #errors()
