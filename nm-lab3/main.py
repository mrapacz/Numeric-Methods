from math import sqrt

import numpy as np
import scipy as sp

from functions import func, derivative, first_stop_criteria, dfa, fa, second_stop_criteria
from newton import newton
from secant import secant


def norm(v1, v2):
    return sqrt(sum([(x1 - x2) ** 2 for x1, x2 in zip(v1, v2)]))


def main():
    rho = 1
    a = -1.8
    b = 0.6

    #for i in np.linspace(-1.7, 0.6, 24):
            #print(rho, i, newton(rho, i, fa, dfa, first_stop_criteria)[1])
        #print(secant(rho, a, i, fa, first_stop_criteria)[1])
    for i in range(16):
        print(i, newton(rho, -1, fa, dfa, first_stop_criteria)[1])
        rho /= 10
def drawfunc():
    for i in np.linspace(-1.8, 0.6, 250):
        print(i, fa(i))
if __name__ == '__main__':
    main()
        # -1.8 + 0.6
