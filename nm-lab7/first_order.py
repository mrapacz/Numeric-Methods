import numpy as np

from drawer import add_to_plot, draw_plot
from equations import calculate_f_x_1
from errors import calculate_mean_square_error, calculate_max_error
from equations import calculate_differential_equation


def euler(k, m, x0, xk, n, h, t, w, x):
    for i in range(0, n):
        w.append(w[i] + h * calculate_differential_equation(t, w[i], k, m))
        t += h
        x.append(t)


def runge_kutta(k, m, x0, xk, n, h, t, w, x):
    for i in range(0, n):
        k1 = calculate_differential_equation(t, w[i], k, m)
        k2 = calculate_differential_equation(t + h / 2, w[i] + k1 * h / 2, k, m)
        k3 = calculate_differential_equation(t + h / 2, w[i] + k2 * h / 2, k, m)
        k4 = calculate_differential_equation(t + h, w[i] + h * k3, k, m)
        w.append(w[i] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        t += h
        x.append(t)


def solve_equation(k, m, x0, xk, n, h, t, w, x, solver, method_name, draw_flag, count):
    solver(k, m, x0, xk, n, h, t, w, x)

    xx = np.linspace(x0, xk, count)
    f_y = [calculate_f_x_1(i, k, m) for i in x]

    mean_square_error = calculate_mean_square_error(x, f_y, w)
    max_error = calculate_max_error(x, f_y, w)
    mean_format = "{:.4f}"
    max_format = "{:.4f}"

    print(";".join((str(n), max_format.format(max_error))))

    if draw_flag:
        add_to_plot(xx, calculate_f_x_1(xx, k, m), "Funkcja")
        add_to_plot(x, w, method_name)
        file_name = method_name + "_" + str(n)
        title = method_name + "  n = " + str(n)
        draw_plot(title, file_name)


if __name__ == '__main__':
    k = 2
    m = 3
    n = 100
    step = 100000
    x0 = np.pi / 6
    xk = 3 * np.pi / 2
    h = (xk - x0) / n
    t = x0

    a = calculate_f_x_1(x0, k, m)
    w = [float(a)]
    x = [float(t)]

    draw_flag = False
    for n in range(1, 200):
        solve_equation(k, m, x0, xk, n, h, t, w, x, euler, "Euler", draw_flag, step)
