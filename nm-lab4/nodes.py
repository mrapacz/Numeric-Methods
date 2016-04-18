import numpy as np
from math import cos, pi


def get_nodes(func, n, a, b):
    return [(i, func(i)) for i in np.linspace(a, b, num=n)]

def get_hermite_nodes(func, derivative, n, a, b):
    return [(i, func(i), derivative(i)) for i in np.linspace(a, b, num=n)]

def get_czebyshev(func, n, a, b):
    l = [(a + b) / 2 + cos(pi * (2 * k - 1) / (2 * n)) * (b - a) / 2 for k in range(1, n + 1)]
    return [(i, func(i)) for i in l]
