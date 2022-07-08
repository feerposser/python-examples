from threading import Thread
import time as t

def thread_method(num, time):
  print("Thread #{} - Hello".format(num))
  t.sleep(time)
  print("Thread #{} - Bye".format(num))

lista = [(1, 2), (2,5), (3,1)]

for tupla in lista:
  a = Thread(target=thread_method, args=(tupla[0], tupla[1]))
  a.start()


# a = Thread(target=thread_method, args=(1, 10))
# b = Thread(target=thread_method, args=(2, 5))

# a.start()
# b.start()

print("\nFim das threads?\n")