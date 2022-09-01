class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


def sort_stack(stack: Stack) -> None:
    if not stack.is_empty():
        temp = stack.pop()
        sort_stack(stack)
        print(stack._items)
        sorted_insert(stack, temp)


def sorted_insert(stack: Stack, value) -> None:
    if stack.is_empty() or value < stack.peek():
        stack.push(value)
    else:
        temp = stack.pop()
        sorted_insert(stack, value)
        stack.push(temp)
