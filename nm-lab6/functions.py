import numpy as np


def values(f, n, a, b):
    return [f(i) for i in np.linspace(a, b, num=n)]
