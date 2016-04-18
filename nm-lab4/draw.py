import random

import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from functions import values

plot_types = ['bo', 'r--', 'k', 'g^']


def draw_func(n, a, b, plotly=False, sepplots=False, coordinates=None, *args):
    func_values = [values(func, n, a, b) for func in args]

    xvalues = values(lambda x: x, n, a, b)

    plt.figure(1)
    i = 211
    j = 0
    for vals in func_values:
        if sepplots:
            plt.subplot(i)
            i += 1
        plt.plot(xvalues, vals, plot_types[j], linewidth=2.0)
        j += 1

    plt.show()

    if not plotly:
        return

    traceNewton = go.Scatter(
        x=xvalues,
        y=func_values[0],
        mode='markers',
        name='Newton'
    )
    traceLagrange = go.Scatter(
        x=xvalues,
        y=func_values[1],
        mode='markers',
        name='Lagrange'
    )
    xi, yi = zip(*coordinates)
    traceCoordinates = go.Scatter(
        x=xi,
        y=yi,
        mode='markers',
        name='Nodes',
        marker=dict(
            size=15,
            color='rgba(0,0,0, 1)'
        )
    )
    if len(args) > 2:
        traceFunc = go.Scatter(
            x=xvalues,
            y=func_values[2],
            mode='markers',
            name='Original function'
        )
    if len(args) > 2:
        data = [traceNewton, traceLagrange, traceFunc, traceCoordinates]
    else:
        data = [traceNewton, traceLagrange, traceCoordinates]

    tls.set_credentials_file(username='mrapacz', api_key='e78ht2ggmf')
    py.plot(data, filename='plot' + str(n))

def draw_func1(n, a, b, func, originalfunc, nodes):
    func_values = values(func, n, a, b)
    print(func_values)
    xvalues = values(lambda x: x, n, a, b)
    xi, yi = zip(*nodes)
    originalvalues = values(originalfunc, n, a, b)
    plt.figure(1)
    plt.plot(xvalues, func_values, plot_types[1], linewidth = 5.0, label="interpolating function")
    plt.plot(xi, yi, plot_types[0], linewidth = 10.0, label="nodes")
    plt.plot(xvalues, originalvalues, 'g--', linewidth = 2.0, label="original function")
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()


def draw_hermite(n, a, b, nodes, *args):
    func_values = [values(func, n, a, b) for func in args]

    xvalues = values(lambda x: x, n, a, b)

    traceHermite = go.Scatter(
        x=xvalues,
        y=func_values[1],
        mode='markers',
        name='Hermite'
    )
    traceFunc = go.Scatter(
            x=xvalues,
            y=func_values[0],
            mode='markers',
            name='Original function'
        )
    xi, yi = zip(*nodes)
    traceCoordinates = go.Scatter(
        x=xi,
        y=yi,
        mode='markers',
        name='Nodes',
        marker=dict(
            size=15,
            color='rgba(0,0,0, 1)'
        )
    )

    data = [traceHermite, traceFunc, traceCoordinates]

    tls.set_credentials_file(username='mrapacz', api_key='e78ht2ggmf')
    py.plot(data, filename='plot' + str(len(nodes)))
