class DoubleConnetedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value


def solution(node):

    if node is None:
        return node

    node.next, node.prev = node.prev, node.next

    if node.prev is None:
        return node

    return solution(node.prev)
