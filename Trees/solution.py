from typing import List


# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: List[List[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below

def pre_order_recursive(root: TreeNode) -> None:
    if root is None:
        return
    print(root.value)
    pre_order_recursive(root.left)
    pre_order_recursive(root.right)


def pre_order_iterative(root: TreeNode) -> None:
    lista = []
    lista.append(root)
    while lista != []:
        son = lista.pop()
        if son is not None:
            print(son.value)
            lista.append(son.right)
            lista.append(son.left)
            
            


def in_order_recursive(root: TreeNode) -> None:
    if root is None:
        return
    in_order_recursive(root.left)
    print(root.value)
    in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
    if root is None:
        return
    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print(root.value)


def breadth_first(root: TreeNode) -> None:
    if root is None:
        return
    lista = []
    lista.append(root)
    while lista != []:
        son = lista.pop(0)
        print(son.value)
        if son.left is not None:
            lista.append(son.left)
        if son.right is not None:
            lista.append(son.right)

def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    if node not in visited:
        print(node.value)
        visited.add(node)
        for i in node.adjacent:
            graph_depth_first_recursive(i, visited)


def graph_depth_first_iterative(node: GraphNode) -> None:
    if node is None:
        return
    visited = set()
    lista = []
    lista.append(node)
    while lista != []:
        son = lista.pop()
        if son not in visited:
            print(son.value)
            visited.add(son)
            for i in son.adjacent:
                lista.append(i)




def graph_breadth_first(node: GraphNode) -> None:
    if node is None:
        return
    visited = set()
    lista = []
    lista.append(node)
    while lista != []:
        son = lista.pop(0)
        if son not in visited:
            print(son.value)
            visited.add(son)
            for i in son.adjacent:
                lista.append(i)


tree = Tree(list(range(15)))
