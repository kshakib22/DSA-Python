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


bst = BSTNode(25)
bst.insertNode(bst, 12)
bst.insertNode(bst, 30)
bst.insertNode(bst, 26)
bst.insertNode(bst, 13)

print(bst)
