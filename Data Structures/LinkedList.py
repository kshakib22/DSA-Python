class Node:

  def __init__(self, value) -> None:
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self):
    current = self.head
    result = ''
    while current is not None:
      result += str(current.value)
      if current.next is not None:
        result += '->'
      current = current.next
    return result

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

    self.length += 1

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node

    self.length += 1

  def insert(self, value, index):
    new_node = Node(value)
    # invalid index
    if index < 0 or index > self.length:
      return False
    # insert at index 0
    if index == 0:
      new_node.next = self.head
      self.head = new_node

    # insert on empty list
    elif self.head is None:
      self.head = new_node
      self.tail = new_node
    # insert in middle somewhere
    else:
      current = self.head
      for _ in range(index - 1):
        current = current.next
      new_node.next = current.next
      current.next = new_node
    self.length += 1
    return True

  def traverse(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next

  def search(self, value):
    current = self.head
    index = 0
    while current:
      if current.value == value:
        return index
      current = current.next
      index += 1
    return -1

  def get(self, index):
    if index == -1:
      return self.tail
    if index < -1 or index >= self.length:
      return None
    current = self.head
    for _ in range(index):
      current = current.next
    return current

  def set_value(self, index, value):
    node = self.get(index)
    if node:
      node.value = value
      return True
    return None

  def pop_first(self):
    popped_node = self.head
    if popped_node is None:
      return None
    if self.length == 1:
      self.head = None
      self.tail = None
      return popped_node
    self.head = self.head.next
    popped_node.next = None
    self.length -= 1
    return popped_node

  def pop(self):
    if self.head is None:
      return None
    if self.length == 1:
      popped_node = self.tail
      self.head = None
      self.tail = None
      self.length -= 1
      return popped_node
    else:
      current = self.head
      while current.next is not self.tail:
        current = current.next
      popped_node = current.next
      current.next = None
      self.tail = current
      self.length -= 1
      return popped_node

  def remove(self, index):
    if index < -1 or index >= self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == (self.length - 1) or index == -1:
      return self.pop()
    else:
      previous = self.get(index - 1)
      current = previous.next
      previous.next = current.next
      current.next = None
      self.length -= 1
      return current

  def delete_all(self):
    self.head = None
    self.tail = None
    self.length = 0

  def reverse(self):
    prev = None
    curr = self.head
    while curr:
      # SAVE NEXT IN TEMP
      temp = curr.next
      # current point to previous element
      curr.next = prev
      # previous now moves to current
      prev = curr
      # current now moves to temp to continue iteration
      curr = temp
    self.tail = self.head
    self.head = prev

  def find_middle(self):
    current = self.head
    index = self.length // 2
    for _ in range(index):
      current = current.next
    return current

  def remove_duplicates(self):
    if self.head is None:
      return None
    else:
      values = set()
      current = self.head
      values.add(current.value)
      while current.next:
        if current.next.value in values:
          current.next = current.next.next
          self.length -= 1
        else:
          values.add(current.next.value)
          current = current.next


lis1 = LinkedList()
lis1.append(123)
lis1.append(3)
lis1.append(3)
lis1.append(78)
lis1.prepend(420)
lis1.insert(420, 0)
print(lis1)

print(lis1.find_middle().value)
lis1.remove_duplicates()
print(lis1)
