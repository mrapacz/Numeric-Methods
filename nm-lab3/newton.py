def newton_formula(f, df, x):
    return x - (f(x) / df(x))


def newton(rho, x, f, df, stop_criteria):
    it = 0
    prevx = x
    x = newton_formula(f, df, x)
    while not stop_criteria(f, x, prevx, rho):
        prevx = x
        x = newton_formula(f, df, prevx)
        it += 1
    return x, it
