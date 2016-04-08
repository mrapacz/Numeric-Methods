def secant_formula(f, a, b):
    return b - ((f(b) * (b - a)) / (f(b) - f(a)))


def secant(rho, a, b, f, criteria):
    it = 0
    while not criteria(f, b, a, rho):
        b, a = secant_formula(f, a, b), b
        it += 1
    return b, it
