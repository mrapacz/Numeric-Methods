from math import e


def func(x):
    return (x ** 4) - 1


def derivative(x):
    return 4 * (x ** 3)


def fa(x):
    return (x ** 12) - ((1 - x) ** 15)


def dfa(x):
    return 12 * (x ** 11) + 15 * (1 - x) ** 14


def first_stop_criteria(f, x, prevx, rho):
    return abs(f(x)) < rho


def second_stop_criteria(f, x, previousx, rho):
    return abs(x - previousx) < rho
