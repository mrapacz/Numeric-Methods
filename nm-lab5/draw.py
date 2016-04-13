import random
import matplotlib.pyplot as plt
import numpy as np
from functions import values

plot_types = ['bo', 'r--', 'k', 'g^']


def draw_func(n, a, b, func):
    func_values = values(func, n, a, b)
    xvalues = values(lambda x: x, n, a, b)

    plt.figure(1)
    plt.plot(xvalues, func_values, plot_types[1], linewidth=2.0)
    plt.show()