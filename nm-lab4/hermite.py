import numpy as np

# based on algorithm found on stack exchange
def hermite(nodes, derivative):
    xi, yi = zip(*nodes)
    n = len(nodes)
    T = np.zeros(shape=(2 * n + 1, 2 * n + 1))

    for i in range(n):
        T[2 * i][0] = xi[i]
        T[2 * i + 1][0] = xi[i]
        T[2 * i][1] = yi[i]
        T[2 * i + 1][1] = yi[i]
        T[i * 2 + 1][2] = derivative(xi[i])

    for j in range(2, 2 * n + 1):
        for i in range(j - 1, 2 * n):
            if j == 2 and i % 2 == 0 or j != 2:
                T[i][j] = (T[i][j - 1] - T[i - 1][j - 1]) / (
                    T[i][0] - T[(i - j + 1)][0])

    def hermite_interpolation(x):
        result = 0
        for i in range(0, 2 * n):
            factor = 1
            j = 0
            while j < i:
                factor *= (x - xi[j // 2])
                if j + 1 != i:
                    factor *= (x - xi[j // 2])
                    j += 1
                j += 1
            result += factor * T[i][i + 1]
        return result

    return hermite_interpolation
