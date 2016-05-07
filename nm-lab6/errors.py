def mean_error(a, b):
    return (sum((x - y) ** 2 for x, y in zip(a, b)))/len(a)


def max_error(a, b):
    return max(abs(x - y) for x, y in zip(a, b))
