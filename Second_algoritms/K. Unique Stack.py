class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class StackSet(Stack):
    def __init__(self):
        super().__init__()
        self.unique_stack = set()

    def push(self, item):
        if item not in self.unique_stack:
            self.unique_stack.add(item)
            return super().push(item)

    def pop(self):
        if self.is_empty():
            print('error')
            return
        else:
            item = super().pop()
            self.unique_stack.remove(item)

    def peek(self):
        if self.is_empty():
            print('error')
            return
        else:
            return super().peek()

    def size(self):
        if self.is_empty():
            return None
        return len(self.unique_stack)


def solution(commands):
    unique_stack = StackSet()

    for _ in range(commands):
        commands = input()

        if commands == 'size':
            print(unique_stack.size())
        elif commands == 'pop':
            unique_stack.pop()
        else:
            unique_stack.push(int(commands.split()[-1]))


if __name__ == '__main__':
    solution(int(input()))
