class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    stack = [(root, False, 0)]

    while stack:
        node, visited, height = stack.pop()

        if node is None:
            continue

        if visited:
            left_height = 0 if node.left is None else node.left.height
            right_height = 0 if node.right is None else node.right.height

            if abs(left_height - right_height) > 1:
                return False

            node.height = max(left_height, right_height) + 1
        else:
            stack.append((node, True, height))
            if node.right:
                stack.append((node.right, False, height + 1))
            if node.left:
                stack.append((node.left, False, height + 1))

    return True


if __name__ == "__main__":
    root1 = BinaryTree(50)
    root1.left = BinaryTree(17)
    root1.right = BinaryTree(76)
    root1.left.left = BinaryTree(9)
    root1.left.right = BinaryTree(23)
    root1.left.left.right = BinaryTree(14)
    root1.left.right.left = BinaryTree(19)
    root1.left.left.right.left = BinaryTree(12)
    root1.right.left = BinaryTree(54)
    root1.right.left.right = BinaryTree(72)
    root1.right.left.right.left = BinaryTree(62)
    print(is_balanced(root1))

    root2 = BinaryTree(50)
    root2.left = BinaryTree(17)
    root2.right = BinaryTree(72)
    root2.left.left = BinaryTree(12)
    root2.left.right = BinaryTree(23)
    root2.left.left.right = BinaryTree(14)
    root2.left.left.left = BinaryTree(9)
    root2.left.right.left = BinaryTree(19)
    root2.right.left = BinaryTree(54)
    root2.right.left.right = BinaryTree(67)
    root2.right.right = BinaryTree(76)
    print(is_balanced(root2))
