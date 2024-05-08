class Stack:

  def __init__(self):
    self.list = []

  def __str__(self):
    values = [str(x) for x in reversed(self.list)]
    return "\n".join(values)

  def isEmpty(self):
    if self.list == []:
      return True
    else:
      return False

  def push(self, value):
    self.list.append(value)

  def pop(self):
    if self.isEmpty:
      return "Stack already empty"
    else:
      self.list.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    else:
      return self.list[-1]

  def delete(self):
    self.list = []


stacc = Stack()

stacc.push(12)
stacc.push(14)
stacc.push(16)
print(stacc)
print(stacc.peek())
stacc.delete()
print(stacc.isEmpty())
