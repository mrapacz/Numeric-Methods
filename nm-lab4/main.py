import math
from interpolate import newton, lagrange
from functions import func
from nodes import get_czebyshev
from draw import draw_func


def main():
    coordinates = get_czebyshev(lambda x: math.cos(math.sin(x))*2 -1, 20, 0, 10)
    print(coordinates)
    x = newton(coordinates)
    print("Finished interpolating with Newton's method.")
    y = lagrange(coordinates)
    print("Finished interpolating with Lagrange's method.")
    print("Drawing plot now...")
    draw_func(100, 0, 10, False, x, y)


if __name__ == '__main__':
    main()
