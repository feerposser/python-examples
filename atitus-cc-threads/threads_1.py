from threading import Thread
import time

class T(Thread):

  def __init__(self, num, time):
    Thread.__init__(self)
    self.num = num
    self.time = time

  def run(self):
    print("Thread #{} - Hello".format(self.num))
    time.sleep(self.time)
    print("Thread #{} - Bye".format(self.num))


a = T(1, 10)
a.start()

b = T(2, 5)
b.start()