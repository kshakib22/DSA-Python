from collections import deque


class BSTNode:
    # from AI to print the BST
    def __str__(self):
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.rightChild is None and self.leftChild is None:
            line = "%s" % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.rightChild is None:
            lines, n, p, x = self.leftChild._display_aux()
            s = "%s" % self.data
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.leftChild is None:
            lines, n, p, x = self.rightChild._display_aux()
            s = "%s" % self.data
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.leftChild._display_aux()
        right, m, q, y = self.rightChild._display_aux()
        s = "%s" % self.data
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    # Our code starts from here
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertNode(self, root, data):
        if root is None:
            root.data = data
        # if data is <= root, it goes left
        elif data <= root.data:
            if root.leftChild is None:
                root.leftChild = BSTNode(data)
            else:
                self.insertNode(root.leftChild, data)
        # if data is > root, it goes right
        else:
            if root.rightChild is None:
                root.rightChild = BSTNode(data)
            else:
                self.insertNode(root.rightChild, data)

    def preOrderTraversal(self, root):
        if root is None:
            return "Empty"
        print(root.data)
        self.preOrderTraversal(root.leftChild)
        self.preOrderTraversal(root.rightChild)

    def inOrderTraversal(self, root):
        if root is None:
            return "Empty"
        self.inOrderTraversal(root.leftChild)
        print(root.data)
        self.inOrderTraversal(root.rightChild)

    def postOrderTraversal(self, root):
        if root is None:
            return "Empty"
        self.postOrderTraversal(root.leftChild)
        self.postOrderTraversal(root.rightChild)
        print(root.data)

    def levelOrderTraversal(self, root):
        if root is None:
            return "Empty"
        track = deque()
        track.append(root)
        while track:
            root = track.popleft()
            print(root.data)
            if root.leftChild:
                track.append(root.leftChild)
            if root.rightChild:
                track.append(root.rightChild)

    def search(self, root, find):
        if root is None:
            print(f"{find} not found")
            return False
        if root.data == find:
            print(f"{find} found")
            return True
        elif find < root.data:
            self.search(root.leftChild, find)
        elif find > root.data:
            self.search(root.rightChild, find)
        else:
            print(f"{find} not found")
            return False


bst = BSTNode(25)
bst.insertNode(bst, 12)
bst.insertNode(bst, 30)
bst.insertNode(bst, 26)
bst.insertNode(bst, 13)
bst.insertNode(bst, 10)
bst.insertNode(bst, 42)

bst.search(bst, 26)
# print(bst)
# print("\n")
# bst.levelOrderTraversal(bst)
