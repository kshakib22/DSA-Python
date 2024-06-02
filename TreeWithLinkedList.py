# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs


class TreeNode:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


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


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.left = leftChild
newBT.right = rightChild

print("\n In Order would be: \n")
inOrderTraversal(newBT)

print("\n Post Order would be: \n")
postOrderTraversal(newBT)
