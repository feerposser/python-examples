from functools import lru_cache
import time


@lru_cache(maxsize=300000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


start = time.time()

for n in range(1, 400000):
    # print(n, ":", fibonacci(n))
    fibonacci(n)

stop = time.time()
print("time:", stop - start)
