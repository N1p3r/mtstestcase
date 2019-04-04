import logging
from functools import wraps


logging.basicConfig(level=logging.INFO, format='(%(asctime)s).%(name)s: %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("LinkedList")


def add(func):
    @wraps(func)
    def wrap(cls, val):
        log.info(f"{func.__name__}ing value {val} to {cls.__class__.__name__}")
        func(cls, val)
    return wrap

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
        else:
            raise StopIteration

    def __next__(self):
        current = self.head
        while current:
            yield current
            current = current.next
        else:
            raise StopIteration

    def unshift(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            node = Node(value, self.head)
            self.head = node

    @add
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value)

