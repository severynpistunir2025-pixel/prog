from typing import List, Optional

class BinaryTree:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root: Optional[BinaryTree]) -> List[int]:
    if root is None:
        return []
    
    result = []
    result.append(root.value)
    result.extend(pre_order_traversal(root.left))
    result.extend(pre_order_traversal(root.right))
    
    return result


root = BinaryTree(1)

root.left = BinaryTree(2)
root.right = BinaryTree(4)

root.left.left = BinaryTree(7)
root.left.right = BinaryTree(10)
root.right.right = BinaryTree(3)

root.left.left.left = BinaryTree(6)
root.left.right.left = BinaryTree(5)
root.left.right.right = BinaryTree(11)

root.left.left.left.right = BinaryTree(8)


print(pre_order_traversal(root))