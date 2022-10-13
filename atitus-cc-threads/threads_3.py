from threading import Thread
import time

class T(Thread):

  def __init__(self, thread, time):
    Thread.__init__(self)
    self.thread = thread
    self.time = time
    self.value = 0

  def run(self):
    print("Thread #{} - Hello".format(self.thread))
    time.sleep(self.time)
    self.set_value(10)
    print("Thread #{} - Bye".format(self.thread))

  def set_value(self, value):
    self.value = value
  
  def get_value(self):
    return self.value


a = T("A", 10)
a.start()
a.join()
print("Valor de A: {}".format(a.get_value()))

b = T("B", 5)
b.start()
b.join()
print("Valor de B: {}".format(b.get_value()))