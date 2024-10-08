import random
import time

# a = [2, 1, 3, 4, 6]
a = [random.randint(1, 1000) for i in range(5_000_000)]


def quick_sort_2(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = lst[len(lst) // 2]
        equal = [x for x in lst if x == mid]
        less = [x for x in lst if x < mid]
        greater = [x for x in lst if x > mid]
        return quick_sort_2(less) + equal + quick_sort_2(greater)


start = time.time()
res = quick_sort_2(a)
finish = time.time()
print("duration_2:", finish - start)

