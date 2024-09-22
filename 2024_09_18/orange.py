def gcd(a, b):
    while b != 0 and a != 0:
        b = b % a
        b, a = a, b
    return b


n, m = [int(s) for s in input("").split()]

res = int((n * m) / gcd(n, m) / m)
print(res)
