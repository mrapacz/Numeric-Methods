import random
import matplotlib.pyplot as plt
import numpy as np
from functions import values

plot_types = ['bo', 'r--', 'k', 'g^']


def draw_func(n, a, b, func, originalfunc, nodes):
    func_values = values(func, n, a, b)
    xvalues = values(lambda x: x, n, a, b)
    xi, yi = zip(*nodes)
    originalvalues = values(originalfunc, n, a, b)
    plt.figure(1)
    plt.plot(xvalues, func_values, plot_types[1], linewidth = 2.0, label="spline function")
    plt.plot(xi, yi, plot_types[0], linewidth = 10.0, label="nodes")
    plt.plot(xvalues, originalvalues, 'g--', linewidth = 2.0, label="original function")
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()