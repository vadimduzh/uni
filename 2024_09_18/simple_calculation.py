n, k = [int(s) for s in input("").split()]

sum = 0
mult = 1
while n > 0:
    rem = n % k
    sum += rem
    mult *= rem
    n = n // k

print(mult - sum)

