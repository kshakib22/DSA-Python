class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    cur = self.head
    while cur:
      yield cur.value
      cur = cur.next

  # def __str__(self):
  #   current = self.head
  #   result = ''
  #   while current is not None:
  #     result += str(current.value)
  #     if current.next is not None:
  #       result += '->'
  #     current = current.next
  #   return result


class Stack:

  def __init__(self):
    self.link = LinkedList()

  def __str__(self):
    values = [str(x) for x in self.link]
    return "\n".join(values)
    

  def isEmpty(self):
    if self.link.head is None:
      return True
    else:
      return False

  def push(self, value):
    new_node = Node(value)
    new_node.next = self.link.head
    self.link.head = new_node

  def peek(self):
    if self.isEmpty():
      print("Stack is empty")
    else:
      print(self.link.head.value)

  def pop(self):
    if self.isEmpty():
      return "The Stack is already empty"
    else:
      nodeVal = self.link.head.value
      self.link.head = self.link.head.next
      return nodeVal

  def delete(self):
    self.link.head = None


stac = Stack()
stac.push(12)
stac.push(13)
stac.push(14)
print(stac)
stac.pop()
print(stac)

