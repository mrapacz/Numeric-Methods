# used pseudocode found in Kincaid
import bisect

import numpy as np


def natural(nodes):
    xi, yi = zip(*nodes)
    n = len(nodes)

    u = [0]
    v = [0]

    h = [xi[i + 1] - xi[i] for i in range(n - 1)]
    b = [6 * (yi[i + 1] - yi[i]) / h[i] for i in range(n - 1)]

    u.append(2 * (h[0] + h[1]))
    v.append(b[1] - b[0])

    for i in range(2, n - 1):
        u.append(2 * (h[i - 1] + h[i]) - (h[i - 1] ** 2) / u[i - 1])
        v.append((b[i] - b[i - 1]) - (h[i - 1] * v[i - 1] / u[i - 1]))

    z = [0 for i in range(n)]
    print(z)

    for i in range(n - 2, 0, -1):
        z[i] = ((v[i] - h[i] * z[i + 1]) / u[i])

    z[0] = 0
    return z


def not_a_knot(nodes):
    n = len(nodes)
    xi, yi = zip(*nodes)
    B = [0]
    A = np.zeros(shape=(n, n))

    h = [xi[i + 1] - xi[i] for i in range(n - 1)]
    b = [6 * (yi[i + 1] - yi[i]) / h[i] for i in range(n - 1)]

    A[0][0:3] = h[1], h[1] - h[0], h[0]

    for i in range(1, n - 1):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        B.append(b[i] - b[i - 1])

    B.append(0)

    A[n - 1][n - 3] = h[n - 2]
    A[n - 1][n - 2] = - h[n - 2] - h[n - 3]
    A[n - 1][n - 1] = h[n - 3]

    z = np.linalg.solve(A, B)
    return z


def get_cubic_f(nodes, zmethod):
    z = zmethod(nodes)
    xi, yi = zip(*nodes)

    h = [xi[i + 1] - xi[i] for i in range(len(nodes) - 1)]

    def spline_function(x):
        i = bisect.bisect_left(xi, x) - 1
        if xi[0] == x:
            i = 0

        a = (z[i + 1] - z[i]) / (6 * h[i])
        b = z[i] / 2
        c = -(h[i] * (z[i + 1] + 2 * z[i])) / 6 + (yi[i + 1] - yi[i]) / h[i]

        # print(z)
        result = yi[i]
        result += ((x - xi[i]) * (c + (x - xi[i]) * (b + (x - xi[i]) * a)))
        return result

    return spline_function
