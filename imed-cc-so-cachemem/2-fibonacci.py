import time


cache = {}


def fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    cache[n] = value
    return value


start = time.time()

for n in range(1, 100000):
    # print(n, ":", fibonacci(n))
    fibonacci(n)

stop = time.time()
print("time:", stop - start)
