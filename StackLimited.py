class Stack:

  def __init__(self, maxSize) -> None:
    self.list = []
    self.maxSize = maxSize

  def __str__(self):
    values = [str(x) for x in reversed(self.list)]
    return "\n".join(values)

  def isEmpty(self):
    if self.list == []:
      return True
    else:
      return False

  def isFull(self):
    if len(self.list) == self.maxSize:
      return True
    else:
      return False

  def push(self, value):
    if self.isFull():
      return "Stack is full"
    else:
      self.list.append(value)

  def pop(self):
    if self.isEmpty():
      return "Stack is already empty"

    else:
      self.list.pop()

  def peek(self):
    print(self.list[-1])

  def delete(self):
    self.list = []


limited_stack = Stack(3)
limited_stack.push(12)
limited_stack.push(13)
limited_stack.push(14)
print(limited_stack.push(15))
print(limited_stack)
limited_stack.pop()
print(limited_stack)
limited_stack.peek()
