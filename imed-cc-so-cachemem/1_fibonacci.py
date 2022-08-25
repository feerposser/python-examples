import time
import os

caminho = os.path.join(str(os.getcwd()), "cache", "cache.txt")


def func1():
    with open("E:\imed-cc-so-cachemem\cache\\cache.txt", 'r') as file:
        print("caminho: ", file.name)
        print(file.read())


def read_cache():
    with open(caminho, 'r') as file:
        cache = {}
        # return [cache.update({int(i): int(k)}) if i not in cache else cache for i, k in
        # [l.split(" ") for l in file.read().split("\n")]]

        lista = [values for values in [lista for lista in [l.split(" ") for l in file.read().split("\n")]]]
        lista.pop(-1)

        try:
            for i, j in lista:
                if i not in cache:
                    cache.update({int(i): int(j)})
            return cache
        except ValueError as e:
            print("Erro de leitura", e)
            return {}


def write_in_cache(item, valor):
    lines = open(caminho, 'r').readlines()

    with open(caminho, 'w') as file:
        for line in lines:
            file.write(line)
        file.write(str(item) + " " + str(valor) + "\n")


def fibonacci(n):
    caching = read_cache()
    if n in caching:
        return caching[n]

    value = 0
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    write_in_cache(n, value)
    return value


start = time.time()

for n in range(1, 10000):
    print(n, ":", fibonacci(n))

stop = time.time()
print("time:", stop - start)
