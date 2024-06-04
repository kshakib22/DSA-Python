from collections import deque


# helper print for debug
def print_deque(deque):
  """Prints the elements of a deque."""
  for element in deque:
    print(element, end=" ")


class TreeNode:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def __str__(self) -> str:
    return str(self.data)


def preOrderTraversal(rootnode):
  # Base case - check if this node is null
  if rootnode is None:
    return
  # We print the data of the current node
  print(rootnode.data)
  # First we go through left subtree
  preOrderTraversal(rootnode.left)
  # Then we go through right subtree
  preOrderTraversal(rootnode.right)


def inOrderTraversal(rootnode):
  if rootnode is None:
    return
  inOrderTraversal(rootnode.left)
  print(rootnode.data)
  inOrderTraversal(rootnode.right)


def postOrderTraversal(rootnode):
  if rootnode is None:
    return
  postOrderTraversal(rootnode.left)
  postOrderTraversal(rootnode.right)
  print(rootnode.data)


def levelOrderTraversal(rootnode):
  if rootnode is None:
    return
  else:
    queue = deque()
    queue.append(rootnode)
    while queue:
      current = queue.popleft()
      print(current.data)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)


def BFS(rootnode, val):
  if rootnode is None:
    return False
  queue = deque()
  queue.append(rootnode)
  while queue:
    current = queue.popleft()
    if current.data == val:
      print("Value found")
      return True
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  print("Value not found")
  return False


def insertNode(rootnode, val):
  if rootnode is None:
    rootnode.data = val
  q = deque()
  q.append(rootnode)
  while q:
    popped = q.popleft()
    if popped.left:
      q.append(popped.left)
    else:
      popped.left = TreeNode(val)
      return True
    if popped.right:
      q.append(popped.right)
    else:
      popped.right = TreeNode(val)
      return True


# Setting up an  example tree
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)



# print("\n Pre Order would be: \n")
# preOrderTraversal(root)

# print("\n In Order would be: \n")
# inOrderTraversal(root)

# print("\n Post Order would be: \n")
# postOrderTraversal(root)

print("\n Level Order would be: \n")
levelOrderTraversal(root)

# BFS(root, 17)
insertNode(root, 5)

print("\n Level Order would be: \n")
levelOrderTraversal(root)