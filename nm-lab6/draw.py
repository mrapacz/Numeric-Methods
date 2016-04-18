from functions import values
import matplotlib.pyplot as plt

plot_types = ['ko', 'r--', 'k', 'g^']


def draw_func(n, a, b, func, originalfunc, nodes):
    func_values = values(func, n, a, b)
    print(func_values)
    xvalues = values(lambda x: x, n, a, b)
    xi, yi = zip(*nodes)
    originalvalues = values(originalfunc, n, a, b)
    plt.figure(1, figsize=(20,10))
    plt.plot(xvalues, func_values, plot_types[1], linewidth=3.0, label="interpolating function")
    plt.plot(xi, yi, plot_types[0], markersize=10.0, label="nodes")
    plt.plot(xvalues, originalvalues, 'g--', linewidth=3.0, label="original function")
    plt.grid(True)
    plt.ylabel('Wartości funkcji')
    plt.xlabel('Argumenty')

    plt.legend(loc='upper left')
    plt.show()
