import unittest
from is_balanced_binary_tree import *


class TestIsBalancedBinaryTree(unittest.TestCase):

    def test1(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        result = is_balanced(root)
        self.assertTrue(result)

    def test2(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        result = is_balanced(root)
        self.assertTrue(result)

    def test3(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.left.left.left = BinaryTree(6)
        result = is_balanced(root)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
