import numpy as np


def get_matrix(n):
    M = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i][j] = 5
            elif j > i:
                sign = -1 if j % 2 == 0 else 1
                M[i][j] = sign * 0.5 / (j + 1)
            elif j == i - 1:
                M[i][j] = 0.5 / (i + 1)
            else:
                M[i][j] = 0
    return M


def get_spectral_radius(M):
    w, v = np.linalg.eig(M)
    return max(np.absolute(w))

def diag(M):
    M = M.copy()
    rows,columns = M.shape
    for i in range(rows):
        for j in range(columns):
            if i != j:
                M[i][j] = 0
    return M
def r_matr(M):
    M = M.copy()
    rows,columns = M.shape
    for i in range(rows):
        for j in range(columns):
            if i == j:
                M[i][j] = 0
    return M
def get_iteration_matrix(M):
    D = diag(M)
    R = r_matr(M)
    D = np.linalg.inv(D)
    iterMatrix = np.dot(D,R)
    return iterMatrix

if __name__ == '__main__':
    for i in range(1,201):
        M = get_matrix(i)
        print(str(i) + ":" + str(get_spectral_radius(get_iteration_matrix(M))))
