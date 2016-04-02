import numpy as np


def taskone(n):
    M = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            if (i == 0):
                M[i][j] = 1
            else:
                M[i][j] = 1 / (i + j + 1)
    return M


def tasktwo(n):
    M = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            if (j >= i):
                M[i][j] = 2 * (i + 1) / (j + 1)
            else:
                M[i][j] = M[j][i]
    return M


def getcond(M):
    return np.linalg.cond(M)


if __name__ == '__main__':
    avg = np.mean([getcond(tasktwo(i)) for i in range(1,101)])
    print(avg)