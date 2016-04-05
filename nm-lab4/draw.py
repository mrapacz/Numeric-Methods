import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls


def values(f, n, a, b):
    return [f(i) for i in np.linspace(a, b, num=n)]


def draw_func(n, a, b, plotly, fa, fb):
    points_fa = values(fa, n, a, b)
    points_fb = values(fb, n, a, b)
    xvalues = values(lambda x: x, n, a, b)
    plt.plot(xvalues, points_fa, 'r--', xvalues, points_fb, 'bs')
    plt.show()

    if not plotly:
        return

    traceNewton = go.Scatter(
        x=xvalues,
        y=points_fa,
        mode='markers'
    )
    traceLagrange = go.Scatter(
        x=xvalues,
        y=points_fb,
        mode='markers'
    )
    data = [traceNewton, traceLagrange]
    tls.set_credentials_file(username='mrapacz', api_key='e78ht2ggmf')
    py.plot(data, filename='test')
