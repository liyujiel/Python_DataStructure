"""

pq.py

Priority Queue Implementation

Ref: https://github.com/mjwestcott/priorityqueue/blob/master/priorityqueue.py

Usage:

    >>> from pq import MinHeapPriorityQueue


"""

class MinHeapPriorityQueue:
    def __init__(self, items):
        self._items = items

