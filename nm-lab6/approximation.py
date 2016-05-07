import numpy as np


def sk(xi, k):
    return sum([x ** k for x in xi])


def tk(xi, yi, k):
    return sum([(x ** k) * y for x, y in zip(xi, yi)])


def approximate(nodes, m):
    xi, yi = zip(*nodes)

    A = np.zeros(shape=(m + 1, m + 1))
    for i in range(0, m + 1):
        for j in range(0, m + 1):
            A[i][j] = sk(xi, i + j)

    B = [tk(xi, yi, k) for k in range(m + 1)]

    factors = np.linalg.solve(A, B)

    def approximation(x):
        return sum(factors[i] * (x ** i) for i in range(m + 1))

    return approximation
