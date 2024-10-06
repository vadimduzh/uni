# a = [2, 1, 3, 4, 6]
import random
import time

# n = int(input())
# lst = [int(s) for s in input().split()]

a = [random.randint(1, 1000) for i in range(5_000_000)]


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = lst[len(lst) // 2]
        less = [x for x in lst if x < mid]
        equal = [x for x in lst if x == mid]
        greater = [x for x in lst if x > mid]
        return quick_sort(less) + equal + quick_sort(greater)


start = time.time()
res = quick_sort(a)
finish = time.time()
print("duration:", finish - start)

# print(res)
