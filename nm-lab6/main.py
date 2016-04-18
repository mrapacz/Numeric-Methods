import numpy as np
from draw import draw_func
from approximation import approximate
from nodes import get_nodes

func = lambda x: np.sin(x)

a = 0
b = 10
count = 1000
n = 10 #number of nodes
m = 3 #polynomial


def approx(n, m):
    nodes = get_nodes(func, n, a, b)
    app = approximate(nodes, m)
    draw_func(count, a, b, app, func, nodes)


if __name__ == '__main__':
    approx(n, m)
