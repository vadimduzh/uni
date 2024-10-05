import random
import time

lst = [2, 3, 1, 100, 8, 4]
# n = int(input(""))
# lst = [int(s) for s in input("").split()]
#
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if lst[i] > lst[j]:
#             lst[j], lst[i] = lst[i], lst[j]
#             print(i)

n = len(lst)

lst = [random.randint(1, 10) for i in range(32000)]
n = len(lst)

start = time.time()
for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            lst[j], lst[i] = lst[i], lst[j]
finish = time.time()
print("duration:", finish - start)

print(lst)


