from interpolate import newton, lagrange
from functions import func
from nodes import *
def main():

    coordinates = [(0,0), (1,1), (2,4), (3,9)]
    x = newton(coordinates)
    y = lagrange(coordinates)
    for i in range(10):
        print(x(i), y(i))
    print(get_czebyshev(func, 4, 0, 1))

if __name__ == '__main__':
    main()