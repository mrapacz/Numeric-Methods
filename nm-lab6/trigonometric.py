import numpy as np


def ak(k, n, xi, yi):
    return 2 * sum([yi[i] * np.cos(k * xi[i]) for i in range(n)]) / n


def bk(k, n, xi, yi):
    return 2 * sum([yi[i] * np.sin(k * xi[i]) for i in range(n)]) / n


def trigonometric_approximate(nodes, m):
    xi, yi = zip(*nodes)
    n = len(nodes)

    def approximation(x):
        return ak(0, n, xi, yi) + sum(
            [ak(k, n, xi, yi) * np.cos(k * x) + bk(k, n, xi, yi) * np.sin(k * x) for k in range(1, m + 1)])

    return approximation
