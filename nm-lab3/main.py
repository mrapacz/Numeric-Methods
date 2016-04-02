from math import sqrt

import scipy as sp


def func(x):
    return (x ** 4) - 1


def derivative(x):
    return 4 * (x ** 3)


def norm(v1, v2):
    return sqrt(sum([(x1 - x2) ** 2 for x1, x2 in zip(v1, v2)]))


def newton_formula(f, df, x):
    return x - f(x) / df(x)


def secant_formula(f, a, b):
    return b - ((f(b) * (b - a)) / (f(b) - f(a)))


def secant(rho, a, b, f, criteria):
    it = 0
    while abs(f(b)) > rho:
        b, a = secant_formula(f, a, b), b
        it += 1
    return b, it

def first_stop_criteria(f, x, rho):
    return abs(f(x)) > rho

def newton(rho, x, f, df):
    it = 0
    while first_stop_criteria(f,x,rho):
        x = newton_formula(f, df, x)
        it += 1
    return x, it


def main():
    print(newton(0.0001, 5, func, derivative))
    print(secant(0.0001, 10, 5, func))


if __name__ == '__main__':
    main()
