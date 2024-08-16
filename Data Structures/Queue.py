class Queue:

  def __init__(self):
    self.items = []

  def __str__(self):
    values = [str(x) for x in self.items]
    return '-'.join(values)

  def isEmpty(self):
    if self.items == []:
      return True
    else:
      return False

  def enqueue(self, value):
    self.items.append(value)

  def dequeue(self):
    # provide index to pop
    self.items.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      return self.items[0]


q = Queue()
print(q.isEmpty())
q.enqueue(99)
q.enqueue(93)
q.enqueue(92)
q.dequeue()
print(q)
