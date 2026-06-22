class Node:
    def __init__(self, value, priority):
        self.value, self.priority = value, priority
        self.parent = self.left = self.right = None
        self.color = 0 # 0: RED, 1: BLACK

class RedBlackPriorityQueue:
    def __init__(self):
        self.TNULL = Node(None, None)
        self.TNULL.color = 1
        self.root = self.TNULL

    def insert(self, value, priority):
        node = Node(value, priority)
        node.left = node.right = self.TNULL
        y, x = None, self.root
        while x != self.TNULL:
            y = x
            x = x.left if node.priority >= x.priority else x.right
        node.parent = y
        if y is None: self.root = node
        elif node.priority >= y.priority: y.left = node
        else: y.right = node
        if node.parent: self._fix_insert(node)
        self.root.color = 1

    def peek(self):
        if self.root == self.TNULL: return None
        curr = self.root
        while curr.left != self.TNULL: curr = curr.left
        return (curr.value, curr.priority)

    def pop(self):
        if self.root == self.TNULL: return None
        z = self.root
        while z.left != self.TNULL: z = z.left
        res = (z.value, z.priority)
        self._delete_node(z)
        return res

    def _rotate_l(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left, x.parent = x, y

    def _rotate_r(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL: y.right.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right, x.parent = x, y

    def _fix_insert(self, k):
        while k.parent and k.parent.color == 0:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 0:
                    u.color = k.parent.color = 1
                    k.parent.parent.color = 0
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._rotate_r(k)
                    k.parent.color, k.parent.parent.color = 1, 0
                    self._rotate_l(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 0:
                    u.color = k.parent.color = 1
                    k.parent.parent.color = 0
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._rotate_l(k)
                    k.parent.color, k.parent.parent.color = 1, 0
                    self._rotate_r(k.parent.parent)
            if k == self.root: break

    def _transplant(self, u, v):
        if not u.parent: self.root = v
        elif u == u.parent.left: u.parent.left = v
        else: u.parent.right = v
        v.parent = u.parent

    def _delete_node(self, z):
        y, color_orig = z, z.color
        if z.left == self.TNULL: x = z.right; self._transplant(z, z.right)
        elif z.right == self.TNULL: x = z.left; self._transplant(z, z.left)
        else:
            y = z.right
            while y.left != self.TNULL: y = y.left
            color_orig, x = y.color, y.right
            if y.parent == z: x.parent = y
            else: self._transplant(y, y.right); y.right = z.right; y.right.parent = y
            self._transplant(z, y); y.left = z.left; y.left.parent = y; y.color = z.color
        if color_orig == 1: self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.color == 1:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 0:
                    s.color, x.parent.color = 1, 0
                    self._rotate_l(x.parent); s = x.parent.right
                if s.left.color == 1 and s.right.color == 1:
                    s.color, x = 0, x.parent
                else:
                    if s.right.color == 1:
                        s.left.color, s.color = 1, 0
                        self._rotate_r(s); s = x.parent.right
                    s.color, x.parent.color = x.parent.color, 1
                    s.right.color = 1; self._rotate_l(x.parent); x = self.root
            else:
                s = x.parent.left
                if s.color == 0:
                    s.color, x.parent.color = 1, 0
                    self._rotate_r(x.parent); s = x.parent.left
                if s.right.color == 1 and s.left.color == 1:
                    s.color, x = 0, x.parent
                else:
                    if s.left.color == 1:
                        s.right.color, s.color = 1, 0
                        self._rotate_l(s); s = x.parent.left
                    s.color, x.parent.color = x.parent.color, 1
                    s.left.color = 1; self._rotate_r(x.parent); x = self.root
        x.color = 1