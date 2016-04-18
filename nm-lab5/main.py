import numpy as np
import math
from nodes import get_nodes
from draw import draw_func
import quadratic
import cubic
from cubic import *
from functions import values
from error import maximal_error, mean_squares

a = -5
b = 10
pointcount = 100

f = lambda x: math.sin(4 * x / math.pi) * math.exp(-x / (5 * math.pi))


def draw_plots(n):
    nodes = get_nodes(f, n, a, b)

    func = cubic.get_cubic_f(nodes, cubic.not_a_knot)
    draw_func(pointcount, a, b, func, f, nodes)

    func = cubic.get_cubic_f(nodes, cubic.natural)
    draw_func(pointcount, a, b, func, f, nodes)

    func = quadratic.get_quadratic_f(nodes, quadratic.not_a_knot)
    draw_func(pointcount, a, b, func, f, nodes)

    func = quadratic.get_quadratic_f(nodes, quadratic.natural)
    draw_func(pointcount, a, b, func, f, nodes)


def get_errors():
    count = 100
    error_list = list()
    for n in range(4, 31):
        nodes = get_nodes(f, n, a, b)
        original_values = values(f, count, a, b)

        vals = values(cubic.get_cubic_f(nodes, cubic.not_a_knot), count, a, b)
        cubic_notaknot_mean = mean_squares(original_values, vals)
        cubic_notaknot_max = maximal_error(original_values, vals)

        vals = values(cubic.get_cubic_f(nodes, cubic.natural), count, a, b)
        cubic_natural_mean = mean_squares(original_values, vals)
        cubic_natural_max = maximal_error(original_values, vals)

        vals = values(quadratic.get_quadratic_f(nodes, quadratic.not_a_knot), count, a, b)
        quadratic_notaknot_mean = mean_squares(original_values, vals)
        quadratic_notaknot_max = maximal_error(original_values, vals)

        vals = values(quadratic.get_quadratic_f(nodes, quadratic.natural), count, a, b)
        quadratic_natural_mean = mean_squares(original_values, vals)
        quadratic_natural_max = maximal_error(original_values, vals)

        #error_list.append((n, cubic_notaknot_max, cubic_natural_max, quadratic_notaknot_max, quadratic_natural_max))
        error_list.append((n, cubic_notaknot_mean, cubic_natural_mean, quadratic_notaknot_mean, quadratic_natural_mean))

    error_list.sort(key=lambda x: x[1])
    for i in error_list:
        print(i)

    i,j,k,l = np.mean([x[1] for x in error_list]), np.mean([x[2] for x in error_list]), np.mean([x[3] for x in error_list]), np.mean([x[4] for x in error_list])
    print(i,j,k,l)
if __name__ == '__main__':
    get_errors()