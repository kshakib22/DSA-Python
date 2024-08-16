print("Title: Queue with Capacity/ Circular Queue \n")
'''
Basic Queue Functionality:

A queue follows the First-In-First-Out (FIFO) principle.
Elements are added at the back (enqueue) and removed from the front (dequeue).

Circular Queue Twist:

In a circular queue, the imaginary tail (where elements are added) can wrap back to the beginning of the queue when it reaches the end of the allocated space.
Similarly, the head (where elements are removed) can reach the end of the space and wrap back to the beginning to continue removing elements.

'''


class Queue:

  def __init__(self, maxSize) -> None:
    self.items = maxSize * [None]
    self.maxSize = maxSize
    # both these are index values
    self.start = -1
    self.end = -1

  def __str__(self) -> str:
    values = [str(x) if x is not None else '_' for x in self.items]
    return ' '.join(values)

  def isFull(self):
    if self.end + 1 == self.start:
      return True
    elif self.start == 0 and self.end + 1 == self.maxSize:
      return True
    else:
      return False

  def isEmpty(self):
    if self.start == -1:
      return True
    else:
      return False

  def enqueue(self, value):
    if self.isFull():
      print("Error: Queue is full")
      return
    elif self.isEmpty():
      self.start = 0
      self.end = 0
    else:
      # wrap around
      self.end = (self.end + 1) % self.maxSize
    self.items[self.end] = value
    print("The value of {} has been added to the end".format(value))

  def dequeue(self):
    if self.isEmpty():
      print("Queue is already empty")
      return
    value = self.items[self.start]
    # Dequeue
    self.items[self.start] = None
    if self.start is self.end:
      self.start = -1
      self.end = -1
    else:
      self.start = (self.start + 1) % self.maxSize

    return value

  def peek(self):
    if self.isEmpty():
      print("No element present in queue")
      return
    return self.items[self.start]


q = Queue(3)
q.enqueue(13)
q.enqueue(5)
q.enqueue(5)
print(q)
q.dequeue()
q.dequeue()
q.dequeue()
print(q)
print(q.peek())
