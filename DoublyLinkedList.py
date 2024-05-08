class Node:

  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

  def __str__(self):
    return str(self.value)


class DoublyLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self):
    temp = self.head
    result = ""
    while temp:
      result += str(temp.value)
      if temp.next:
        result += " <-> "
      temp = temp.next
    return result

  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1

  def prepend(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1

  def traverse(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next

  def reverse_traverse(self):
    current = self.tail
    while current:
      print(current.value)
      current = current.prev

  def search(self, target):
    current = self.head
    while current:
      if current.value == target:
        return True
      current = current.next
    return False

  def get(self, index):
    if index < 0 or index >= self.length or self.head is None:
      return None
    elif index <= self.length // 2:
      current = self.head
      for _ in range(index):
        current = current.next
    else:
      current = self.tail
      for _ in range(self.length - 1, index, -1):
        current = current.prev
    return current

  def set(self, index, value):
    node = self.get(index)
    if node:
      node.value = value
      return True
    else:
      return False

  def insert(self, index, value):
    if index < 0 or index > self.length:
      print("Index out of bounds")
      return
    if index == 0:
      self.prepend(value)
      return
    if index == self.length:
      self.append(value)
      return
    new_node = Node(value)
    prev = self.get(index - 1)
    new_node.next = prev.next
    new_node.prev = prev
    prev.next.prev = new_node
    prev.next = new_node
    self.length += 1

  def pop_first(self):
    if not self.head:
      return None
    elif self.length == 1:
      self.head = None
      self.tail = None
    else:
      current = self.head
      self.head = self.head.next
      self.head.prev = None
      current.next = None
    self.length -= 1
    return current

  def pop(self):
    if not self.head:
      return None
    elif self.length == 1:
      self.head = None
      self.tail = None
    else:
      current = self.tail
      self.tail = self.tail.prev
      self.tail.next = None
      current.prev = None
    self.length -= 1
    return current

  def remove(self, index):
    if index < 0 or index >= self.length:
      print("Index out of bounds")
      return
    elif index == 0:
      return self.pop_first()
    elif index == self.length - 1:
      return self.pop()
    else:
      pop_node = self.get(index)
      pop_node.prev.next = pop_node.next
      pop_node.next.prev = pop_node.prev
      pop_node.next = None
      pop_node.prev = None
      self.length -= 1
      return pop_node


dll = DoublyLinkedList()
dll.append(12)
dll.append(13)
dll.append(14)
dll.prepend(11)
dll.prepend(10)
print(dll)
print(dll.set(2, 12.5))
dll.pop_first()
dll.pop()
print(dll)
