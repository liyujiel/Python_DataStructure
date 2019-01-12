class Queue:
    def __init__(self, input_list=list()):
        if not isinstance(input_list, list):
            input_list = list(input_list)
        self._queue = input_list

    def is_empty(self):
        """
        Return True if queue is empty
        :return: Boolean
        """
        return len(self._queue) == 0

    def peek(self):
        """
        :return: queue_item
        """
        return self._queue[0]

    def pop(self):
        """
        :return: queue_item
        """
        if self.is_empty():
            raise ValueError
        pop_item = self.peek()
        self._queue = self._queue[1:]
        return pop_item

    def push(self, item):
        """
        :param item: queue_item
        :return: Boolean if success
        """
        self._queue.append(item)
        return True

    def print_queue(self):
        """
        :return: list
        """
        return print(self._queue)

    def find_item(self, key):
        """
        :param key: queue_item
        :return: int
        """
        for index in range(len(self._queue)):
            if self._queue[index] == key:
                return index
        return -1

    def remove_item(self, key):
        key_pos = self.find_item(key)
        if key_pos != -1:
            self._queue = self._queue[:key_pos] + self._queue[key_pos+1:]
        else:
            print("Remove Item Not Found")
        return True


if __name__ == '__main__':
    queue = Queue()
    queue.push(0)
    queue.print_queue()
    queue.push(1)
    queue.print_queue()
    queue.push(2)
    queue.print_queue()
    queue.pop()
    queue.print_queue()
    queue.peek()
    queue.print_queue()
    queue.push(3)
    queue.print_queue()
    queue.push(3)
    queue.print_queue()
    queue.remove_item(3)
    queue.print_queue()

