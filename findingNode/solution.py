from re import search


class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def in_order_succ(node: TreeNode) -> TreeNode:
    if node == None:
        return None
    if node.right != None:
        lefty = search_left_most(node.right)
        return lefty
    else:
        q = node.parent
        while q != None and q.right == node:
            node = q
            q = q.parent
        return q


def search_left_most(node: TreeNode) -> TreeNode:
    while node.left != None:
        node = node.left
    return node
