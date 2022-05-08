class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution(node, elem):
    index = 0

    while node:
        if node.value == elem:
            return index
        node = node.next_item
        index += 1

    return -1


if __name__ == '__main__':
    n3 = Node('third')
    n2 = Node('second', n3)
    n1 = Node('first', n2)
    print(n1, n2, n3)
    print(n1.next_item)
    print(n2.next_item)

    h = solution(n1, 'first')
    print(h)