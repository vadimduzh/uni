def f(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return f(k - 1) + f(k - 2)


def gcd(a, b):
    while b != 0 and a != 0:
        b = b % a
        b, a = a, b
    return b


a, b = [int(s) for s in input("").split()]

res = f(gcd(a, b))
print(res)

