class MyQueueSized:
    def __init__(self, n):
        self._queue = []
        self.max_n = n

    def is_empty(self):
        return len(self._queue) == 0

    def push(self, item):
        if self.max_n != 0:
            self._queue.append(item)
        else:
            print('error')
            return
        self.max_n -= 1

    def pop(self):
        if self.is_empty():
            return None
        self.max_n += 1
        return self._queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self._queue[0]

    def size(self):
        return len(self._queue)


def solution(commands):
    size_queue = int(input())
    queue = MyQueueSized(size_queue)

    for _ in range(commands):
        command = input().split()

        if command[0] == 'push':
            queue.push(int(command[1]))
        elif command[0] == 'pop':
            print(queue.pop())
        elif command[0] == 'peek':
            print(queue.peek())
        elif command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    solution(int(input()))
