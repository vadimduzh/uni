n, x, y = [int(s) for s in input("").split()]

total_time = 0
if n == 1:
    total_time = min(x, y)
else:
    total_time = min(x, y)

    left = 0
    right = max(x, y) * (n - 1)
    while left < right:
        mid = (left + right) // 2
        copies_count = mid // x + mid // y

        if n - 1 > copies_count:
            left = mid + 1
        else:
            right = mid

    total_time += left
print(total_time)
