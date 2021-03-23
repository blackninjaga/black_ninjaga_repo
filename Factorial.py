def fac(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

def fac_r(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * fac_r(n - 1)


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))

def fib_r(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_r(n - 1) + fib_r(n - 2)


































