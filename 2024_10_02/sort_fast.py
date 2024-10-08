import random
import time


def quick_sort(lst, left, right):
    if left < right:
        middle = lst[(left + right) // 2]
        i, j = left, right
        while i <= j:
            while lst[i] < middle:
                i += 1
            while lst[j] > middle:
                j -= 1

            if i <= j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        quick_sort(lst, left, j)
        quick_sort(lst, i, right)

    return lst


b = [random.randint(1, 1000) for i in range(5_000_000)]

start = time.time()
res = quick_sort(b, 0, len(b) - 1)
finish = time.time()
print("duration:", finish - start)
