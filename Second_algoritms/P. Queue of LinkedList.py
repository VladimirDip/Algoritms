class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def get(self):
        if self.head is None:
            return 'error'
        else:
            to_return = self.head
            self.head = self.head.next_item
            return to_return

    def put(self, item):
        if self.last is None:
            self.head = Node(item)
            self.last = self.head
        else:
            self.last.next_item = Node(item)
            self.last = self.last.next_item

    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next_item
        return count


def main(commands):
    my_queue = Queue()
    for _ in range(commands):
        command = input().split()
        if command[0] == 'get':
            print(my_queue.get())
        elif command[0] == 'size':
            print(my_queue.size())
        elif command[0] == 'put':
            my_queue.put(int(command[1]))


if __name__ == '__main__':
    main(int(input()))
