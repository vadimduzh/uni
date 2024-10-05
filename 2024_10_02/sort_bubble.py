# lst = [2, 3, 1]
n = int(input(""))
lst = [int(s) for s in input("").split()]

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if lst[j] < lst[i]:
            lst[j], lst[i] = lst[i], lst[j]
            count += 1

print(count)
