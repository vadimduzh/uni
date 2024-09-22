def gcd(a, b):
    while b != 0 and a != 0:
        b = b % a
        b, a = a, b
    return b


n_1, n_2 = [int(s) for s in input("").split()]

res = int((n_1 * n_2) / gcd(n_1, n_2) / n_2)
print(res)
