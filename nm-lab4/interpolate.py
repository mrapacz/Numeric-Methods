def newton(points):
    n = len(points)
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

    def p(x):
        sum = 0
        for i in range(k):
            factor = c[i]
            for j in range(i):
                factor *= (x - xi[j])
            sum += factor
        return sum

    return p

def newton_interpolate(points):
    x1, y1 = zip(*points)
    n = len(points)
    dq = list(y1)
    x = list(x1)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            dq[j] = (dq[j] - dq[j - 1]) / (x[j] - x[j - i])

    def result_polynomial(xpoint):
        val = dq[0]
        factor = 1.0
        for i in range(1, n):
            factor *= (xpoint - x[i - 1])
            val += (dq[i] * factor)
        return val

    return result_polynomial

def lagrange_interpolate(points):
    def result_polynomial(x):
        sum = 0
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            product = 1
            for j in range(n):
                if i != j:
                    xj, yj = points[j]
                    product *= (x - xj) / float(xi - xj)
            sum += yi*product
        return sum
    return result_polynomial

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
