
class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def make_list(l: list) -> list[Node]:
    nodes = [Node(v) for v in l]
    for node, next in zip(nodes[:-1], nodes[1:]):
        node.next = next
    return nodes


def find_intersection(head1: Node, head2: Node) -> Node:
    set = {}
    size1 = 0
    size2 = 0
    tail1 = None
    tail2 = None
    while head1:
        if head1.next == None:
            tail1 = head1
        else:
            size1 += 1
        head1 = head1.next

    while head2:
        if head2.next == None:
            tail2 = head2
        else:
            size2 += 1
        head2 = head2.next

    return True


l1 = make_list([4, 7, 1, 9, 4, 5, 3])
l2 = make_list([8, 2])
l2[-1].next = l1[4]


print(find_intersection(l1, l2))
