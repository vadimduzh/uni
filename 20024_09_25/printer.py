n, x, y = [int(s) for s in input("").split()]

res = 0
if n == 1:
    res = min(x, y)
else:
    res = min(x, y)

    left = 0
    right = max(x, y) * (n - 1)
    while left < right:
        mid = (left + right) // 2
        copies_count = mid // x + mid // y

        if n - 1 > copies_count:
            left = mid + 1
        else:
            right = mid

    res += left
print(res)
