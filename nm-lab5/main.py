import numpy as np
import math
from nodes import get_nodes
from draw import draw_func
from quadratic import *
from cubic import *
n = 10
a = -3
b = 3
f = lambda x: x**3
nodes = get_nodes(f, n, a,b)
print(nodes)
x, y = zip(*nodes)
func = get_cubic_f(nodes, not_a_knot)
#func = create_quadratic_function(x,y, calculate_quadratic_value)
func(1)
draw_func(100, a, b, func)