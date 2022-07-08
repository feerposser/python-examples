from multiprocessing import Process
import time as t

def process(value, time):
  print("starting: {}".format(value))
  t.sleep(time)
  print("stoping: {}".format(value))


if __name__ == "__main__":
  a = Process(target=process, args=("A", 30))
  b = Process(target=process, args=("B", 45))

  a.start()
  b.start()

print("EOF")