import math
import numpy as np


def get_jacobi(xs):
    x, y, z = xs
    J = np.zeros((3, 3))
    J[0] = [2 * x, 2 * y, 1]
    J[1] = [4 * x, 2 * y, 3 * (z ** 2)]
    J[2] = [3, -6 * (y ** 2), -4 * z]
    return J


def get_results(xs):
    x, y, z = xs
    return [(x ** 2) + (y ** 2) + z - 1, 2 * (x ** 2) + (y ** 2) + (z ** 3) - 2,
            (3 * x) - 2 * (y ** 3) - 2 * (z ** 2) - 3]


def first_criteria(xs, newxs, rho):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(xs, newxs))) < rho


def second_criteria(xs, newxs, rho):
    return math.sqrt(sum(x ** 2 for x in get_results(xs))) < rho


def solve(xs, criteria, rho, maxit):
    it = 1
    newxs = np.dot(np.linalg.inv(get_jacobi(xs)), get_results(xs)) + xs
    while not criteria(xs, newxs, rho) and it < maxit:
        xs = newxs
        newxs = -np.dot(np.linalg.inv(get_jacobi(xs)), get_results(xs)) + xs
        it += 1
    if it == maxit:
        return -1, newxs
    else:
        return it, newxs

def start(x):
    return [x, x, x]

solve(start(1), second_criteria, 0.01, 1000)