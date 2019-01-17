class Stack:
    def __init__(self, stack_list=list()):
        self._stack = stack_list
        self._len = len(stack_list)

    def is_empty(self):
        return self._len == 0

    def peek(self):
        return self._stack[self._len-1]

    def pop(self):
        if self.is_empty():
            raise ValueError
        self._stack = self._stack[:self._len-2]
        self._len -= 1
        return self.peek()

    def push(self, val):
        self._stack.append(val)
        self._len += 1
        return True

    def print_stack(self):
        print(list(reversed(self._stack)))


if __name__ == '__main__':
    stack = Stack([1, 2, 3, 4])
    stack.print_stack()
