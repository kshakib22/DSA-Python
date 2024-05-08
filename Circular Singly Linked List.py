class Node:

  def __init__(self, value):
    self.data = value
    self.next = None

  def __str__(self):
    return str(self.data)


class CSLinkedList:
  # # Default to a node
  # def __init__(self, value):
  #   new_node = Node(value)
  #   self.head = new_node
  #   self.tail = new_node
  #   new_node.next = new_node
  #   self.length = 1

  # Default to empty
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
      new_node.next = new_node

    else:
      self.tail.next = new_node
      new_node.next = self.head
      self.tail = new_node

    self.length += 1

  def __str__(self) -> str:
    temp = self.head
    result = ""
    while temp:
      result += str(temp.data)
      temp = temp.next
      if temp == self.head:
        break
      result += " -> "
    return result

  def prepend(self, value):
    new_node = Node(value)

    if self.head is None:
      self.head = new_node
      self.tail = new_node
      new_node.next = new_node

    else:
      new_node.next = self.head
      self.head = new_node
      self.tail.next = new_node

    self.length += 1

  def insert(self, index, value):
    if index > self.length or index < 0:
      raise Exception("Index out of range")
    new_node = Node(value)
    if index == 0:
      if self.head is None:
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
      else:
        new_node.next = self.head
        self.head = new_node
        self.tail.next = new_node
    elif index == self.length:
      self.tail.next = new_node
      new_node.next = self.head
      self.tail = new_node
    else:
      temp = self.head
      for _ in range(index - 1):
        temp = temp.next
      new_node.next = temp.next
      temp.next = new_node
    self.length += 1

  def search(self, target):
    current = self.head
    while current:
      if current.data == target:
        return True
      current = current.next
      if current == self.head:
        break
    return False

  def get(self, index):
    if index <-1 or index > self.length:
      return None
    if index == -1:
      return self.tail
    else:
      current = self.head
      for _ in range(index):
        current = current.next
      return current
  def set(self, index, value):
    if index < 0 or index > self.length:
      return False
    else:
      current = self.head
      for _ in range(index):
        current =  current.next
      current.data = value
      return True
  def pop_first(self):
    pop_node = self.head
    if self.head == None:
      return None
    elif self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      self.tail.next = self.head
      pop_node.next = None
    self.length -= 1
    return pop_node

  def pop(self):
    pop_node = self.tail
    if self.tail == None:
      return None
    elif self.length == 1:
      self.head = self.tail = None
    else:
      temp = self.head
      while(temp.next is not self.tail):
        temp = temp.next
      pop_node.next = None
      self.tail = temp
      temp.next = self.head
    self.length -= 1
    return pop_node

  def remove(self, index):
    if self.tail == None:
      return None
    elif index < 0 or index > self.length:
      return Exception("Index out of range")
    elif index == 0:
      return self.pop_first()
    elif index == self.length - 1:
      return self.pop()
    else:
      prev = self.get(index-1)
      pop = prev.next
      prev.next = pop.next
      pop.next = None

    self.length -= 1
    return pop

  def delete(self):
    if self.tail is None:
      return None
    self.tail.next = None
    self.head = None
    self.tail = None
    self.length = 0

  def count(self):
    if self.tail is None:
      return 0
    current = self.head.next
    count = 1
    while current is not self.head:
      count += 1
      current = current.next
    return count

  # def split_list(self):
  #   if self.tail is None:
  #     return None
  #   if self.tail is self.head:
  #     return None
  #   slow = self.head
  #   fast = self.head

  #   while fast.next is not self.head and fast.next.next is not self.head:
  #     slow = slow.next
  #     fast = fast.next.next

  def is_sorted(self):
    if self.tail is None:
      return None
    elif self.head is self.tail:
      return True
    else:
      current = self.head
      while(current):
        if current.data > current.next.data:
          return False
        current = current.next
        if current is self.tail:
          break
      return True

  def insert_into_sorted(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      new_node.next = new_node
    elif data <= self.head.data:
      self.prepend(data)
    else:
      temp = self.head
      while temp.next is not self.head and temp.next.data < data:
        temp = temp.next
      new_node.next = temp.next
      temp.next = new_node

    self.length += 1


mama = CSLinkedList()
mama.insert(0, 10)
mama.append(69)
mama.append(420)
mama.prepend(121)
mama.insert(4, 13)
print(mama.search(69))
print(mama.search(697))
mama.set(4,1313)
print(mama.count())
mama.pop_first()
print(mama)
print(mama.is_sorted())