def count_ones(x):
    count = 0
    while x > 0:
        if x % 2 != 0:
            count += 1
        x = x // 2
    return count


n = int(input(""))
value = count_ones(n)
print(value)
