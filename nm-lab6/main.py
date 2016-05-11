import numpy as np
from draw import draw_func
from approximation import approximate
from nodes import get_nodes
from functions import values
from errors import mean_error, max_error
from trigonometric import trigonometric_approximate

a = -5
b = 10

func = lambda x: np.sin(4 * x / np.pi) * np.exp(-x / (5 * np.pi))

count = 1000
n = 10  # number of nodes
m = 9  # polynomial

error_point_count = 1000


def approx(n, m, method):
    nodes = get_nodes(func, n, a, b)
    app = method(nodes, m)
    draw_func(count, a, b, app, func, nodes)


def geterrors(method, count, n, m):
    nodes = get_nodes(func, n, a, b)
    app = method(nodes, m)

    appvalues = values(app, count, a, b)
    origvalues = values(func, count, a, b)
    mean = mean_error(appvalues, origvalues)
    max = max_error(appvalues, origvalues)
    return (m, mean, max)


if __name__ == '__main__':
    approx(n, m, trigonometric_approximate)
