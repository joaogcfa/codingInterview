from cgitb import small


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def find_intersection(head1: Node, head2: Node) -> Node:
    size1 = 1
    size2 = 1
    l1 = []
    l2 = []

    if head1 == None or head2 == None or head1.next == None or head2.next == None:
        return None

    while head1:
        size1 += 1
        l1.append(head1)
        head1 = head1.next

    while head2:
        size2 += 1
        l2.append(head2)
        head2 = head2.next

    if l1[-1].value != l2[-1].value:
        return None

    ponteiro1 = 0
    ponteiro2 = 0
    dif = size1-size2

    if dif > 0:
        ponteiro1 = dif
    else:
        ponteiro2 = abs(dif)

    while ponteiro1 < len(l1):
        if l1[ponteiro1] == l2[ponteiro2]:
            return l1[ponteiro1]
        ponteiro1 += 1
        ponteiro2 += 1


tail = Node(4, Node(5, Node(3)))
node1 = Node(4, Node(7, Node(1, Node(9, tail))))
node2 = Node(8, Node(2, tail))


find_intersection(node2, node1)
