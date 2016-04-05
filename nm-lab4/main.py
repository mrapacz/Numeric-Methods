import math
from interpolate import newton, lagrange
from functions import func
from nodes import get_czebyshev
from draw import draw_func


def main():
    coordinates = get_czebyshev(lambda x: math.sin(x), 10, 0, 10)
    print(coordinates)
    x = newton(coordinates)
    y = lagrange(coordinates)

    plots = [(i, y(i)) for i in range(100)]
    draw_func(y, 100, 0, 100)


if __name__ == '__main__':
    main()
