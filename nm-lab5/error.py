def classical_squares(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def maximal_error(a, b):
    return max(abs(x - y) for x, y in zip(a, b))
