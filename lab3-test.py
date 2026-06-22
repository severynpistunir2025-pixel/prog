import sys
import os
import unittest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab3 import BinaryTree, pre_order_traversal

class TestTreeTraversal(unittest.TestCase):
    def test_example_tree(self):
        # Будуємо дерево з умови задачі
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        expected = [1, 2, 5, 3, 6, 7]
        self.assertEqual(pre_order_traversal(root), expected)

    def test_empty_tree(self):
        self.assertEqual(pre_order_traversal(None), [])

if __name__ == "__main__":
    unittest.main()