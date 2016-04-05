def newton(points):
    n = len(points)
    print(points)
    xi, yi = zip(*points)
    c = [yi[0]]

    for k in range(1, n):
        def p(x):
            sum = 0
            for i in range(k):
                factor = c[i]
                for j in range(i):
                    factor *= (x - xi[j])
                sum += factor
            return sum

        cc = yi[k] - p(xi[k])
        for j in range(k):
            cc /= (xi[k] - xi[j])
        c.append(cc)
    print(len(c))

    def p(x):
        sum = 0
        for i in range(k):
            factor = c[i]
            for j in range(i):
                factor *= (x - xi[j])
            sum += factor
        return sum

    return p


def lagrange(points):
    n = len(points)
    xi, yi = zip(*points)

    def lag(x):
        res = 0
        for i in range(n):
            lk = yi[i]
            for j in range(n):
                if i == j:
                    continue
                else:
                    lk *= (x - xi[j]) / (xi[i] - xi[j])
            res += lk
        return res

    return lag
