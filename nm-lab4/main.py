import math
from hermite import hermite
from interpolate import newton, lagrange
from functions import values
from nodes import get_czebyshev, get_nodes, get_hermite_nodes
from draw import draw_func, draw_func1, draw_hermite
from error import classical_squares, maximal_error

func = lambda x: math.sin((4 * x) / math.pi) * math.e ** (-0.2 * x / math.pi)
derivative_func = lambda x: (1 / math.pi) * (
    (4 * math.exp(-x / (5 * math.pi))) * math.cos((4 * x) / math.pi) - (1 / 5) * (
        math.exp(-x / (5 * math.pi)) * math.sin((4 * x) / math.pi)))

a = -5
b = 10


def draw_plots(n, nodes):
    coordinates = nodes(func, n, a, b)
    x = newton(coordinates)
    print("Finished interpolating with Newton's method.")
    y = lagrange(coordinates)
    print("Finished interpolating with Lagrange's method.")
    print("Drawing plot now...")
    draw_func(1000, -5, 10, True, False, coordinates, x, y, func)


def get_errors(nodes):
    count = 100
    l = list()
    for n in range(2, 31):
        coordinates = nodes(func, n, a, b)
        x = newton(coordinates)
        y = lagrange(coordinates)
        newtons = values(x, count, a, b)
        lagranges = values(y, count, a, b)
        original = values(func, count, a, b)
        l.append((n, classical_squares(newtons, original), classical_squares(lagranges, original),
                  maximal_error(newtons, original), maximal_error(lagranges, original)))

    l.sort(key=lambda x: x[4])
    print([i[0] for i in l])


def get_hermite(n, nodemethod):
    coordinates = nodemethod(func, n, a, b)
    herm = hermite(coordinates, derivative_func)

    draw_hermite(10000, a, -4, coordinates, func, herm)
    return


def get_hermite_errors(n, nodes):
    count = 100
    l = []
    for n in range(2, 31):
        coordinates = nodes(func, n, a, b)

        herm_func = hermite(coordinates, derivative_func)

        hermites = values(herm_func, count, a, b)
        original = values(func, count, a, b)

        l.append((n, classical_squares(hermites, original), maximal_error(hermites, original)))
    l.sort(key=lambda x: x[2])
    for i in l:
        print(i)


if __name__ == '__main__':
    get_hermite(50, get_czebyshev)
