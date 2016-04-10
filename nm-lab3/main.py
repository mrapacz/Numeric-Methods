from math import sqrt

import numpy as np

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
    rho = 1e-4
    maxit = 10000
    count = 0
    data = list()
    avg = 0
    i = 1
    for i in np.linspace(-100, 100, 10000):
        startvector = [i, i, i]
        ret = -1
        try:
            ret = ss.solve(startvector, ss.first_criteria, rho, maxit)
        except:
            continue
        if ret[0] != -1:
            count += 1
            avg += ret[0]
            # print("result vector:", ret[1], "iteration count:", ret[0], "Start vector:", startvector)
            f.write(str(count) + "\n" + "result vector: " + str(ret[1]) + "\n iteration count: " + str(
                ret[0]) + "\n Start vector: " + str(startvector) + "\n")
    print(count)
    print(avg / 10000)
    f.close()


def task3():
    rho = 1
    maxit = 10000
    startv = [-55.135513551355132, -55.135513551355132, -55.135513551355132]
    for i in range(17):
        print(i, ss.solve(startv, ss.second_criteria, rho, maxit)[0])
        rho /= 10
        # l = [(i,ss.solve([i,i,i], ss.second_criteria, rho, maxit)) for i in np.linspace(-100, 100, 10000)]
        # l.sort(key=(lambda x: x[1][0]))
        # print(l)
        # print(len(l), l[len(l)-1])


if __name__ == '__main__':
    task2()
