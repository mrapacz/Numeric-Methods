import matplotlib.pyplot as plt
import numpy as np


def draw_func(f, n, a, b):
    points = [(i, f(i)) for i in np.linspace(a, b, num=n)]
    x, y = zip(*points)
    plt.plot(x, y)
    plt.show()
