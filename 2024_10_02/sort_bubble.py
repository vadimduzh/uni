import random
import time

# n = int(input())
# lst = [int(s) for s in input().split()]

lst = [random.randint(1, 10) for i in range(32000)]
n = len(lst)

start = time.time()
count = 0
for i in range(n):
    for j in range(n - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            count += 1
finish = time.time()
print("duration:", finish - start)

print(count)

print(lst)
