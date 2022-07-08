import time


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


start = time.time()

for n in range(1, 47):
    print(n, ":", fibonacci(n))

stop = time.time()
print("time:", stop - start)
