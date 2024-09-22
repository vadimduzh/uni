def gcd(a, b):
    while b != 0 and a != 0:
        b = b % a
        b, a = a, b
    return b


a, b = [int(s) for s in input("").split()]

res = gcd(a, b)
print(res)


