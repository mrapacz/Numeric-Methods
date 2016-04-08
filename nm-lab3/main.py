from math import sqrt

import numpy as np
import scipy as sp

from functions import func, derivative, first_stop_criteria, dfa, fa, second_stop_criteria
from newton import newton
from secant import secant

import systemsolver as ss


def norm(v1, v2):
    return sqrt(sum([(x1 - x2) ** 2 for x1, x2 in zip(v1, v2)]))


def task1():
    rho = 1
    a = -1.8
    b = 0.6

    # for i in np.linspace(-1.7, 0.6, 24):
    # print(rho, i, newton(rho, i, fa, dfa, first_stop_criteria)[1])
    # print(secant(rho, a, i, fa, first_stop_criteria)[1])
    for i in range(16):
        print(i, newton(rho, -1, fa, dfa, first_stop_criteria)[1])
        rho /= 10


def task2():
    f = open('system_first.txt', 'w')
    rho = 0.001
    maxit = 10000
    count = 0
    data = list()
    i = 1
    for i in np.linspace(-100, 100, 10):
        startvector = [i, i, i]
        ret = -1
        try:
            ret = ss.solve(startvector, ss.second_criteria, rho, maxit)
        except:
            continue
        if ret[0] != -1:
            count += 1
            print("result vector:", ret[1], "iteration count:", ret[0], "Start vector:", startvector)
            f.write(str(count) + "\n"+  "result vector: " + str(ret[1]) +  "\n iteration count: " + str(ret[0]) + "\n Start vector: " + str(startvector) + "\n")
    print(count)
    f.close()


if __name__ == '__main__':
    task2()
    # -1.8 + 0.6
