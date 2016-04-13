#used pseudocode found in Kincaid
import numpy as np
import bisect


def natural(nodes):
    xi, yi = zip(*nodes)
    n = len(nodes)
    z = [0]

    for i in range(0, n - 1):
        ydiff = yi[i + 1] - yi[i]
        xdiff = xi[i + 1] - xi[i]
        z.append(-z[i] + ((2 * ydiff) / xdiff))
    return z


def not_a_knot(nodes):
    xi, yi = zip(*nodes)
    n = len(nodes)

    B = [(yi[1] - yi[0]) / (xi[1] - xi[0])]

    A = np.zeros(shape=(n, n))
    A[0][0] = 1

    for i in range(1, n):
        A[i][i - 1] = 1
        A[i][i] = 1

        ydiff = yi[i - 1] - yi[i]
        xdiff = xi[i - 1] - xi[i]

        B.append(2 * (ydiff / xdiff))

    return np.linalg.solve(A, B)


def create_quadratic_function(nodes, zmethod):
    z = zmethod(nodes)

    xi, yi = zip(*nodes)

    def quad_spline(x):
        i = bisect.bisect_left(xi, x) - 1
        if xi[0] == x:
            i = 0
        return ((z[i + 1] - z[i]) * (x - xi[i]) * (x - xi[i])) / (2 * (xi[i + 1] - xi[i])) + z[i] * (x - xi[i]) + yi[i]

    return quad_spline
