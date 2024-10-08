import random
import time
lst = [random.randint(1, 10) for i in range(5_000_000)]
start = time.time()
lst.sort()
finish = time.time()
print("duration:", finish - start)
