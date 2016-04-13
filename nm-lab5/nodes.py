import numpy as np


def get_nodes(func, n, a, b):
    return [(i, func(i)) for i in np.linspace(a, b, num=n)]
