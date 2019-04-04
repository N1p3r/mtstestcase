import logging


logging.basicConfig(level=logging.INFO, format='(%(asctime)s).%(name)s: %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("LinkedList")


def push(func):
    def wrap(cls, val):
        log.info(f"Adding element {val} to linked list head")
        func(cls, val)
    return wrap


def unshift(func):
    def wrap(cls, val):
        log.info(f"Deleting element {val} from linked list")
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

    @unshift
    def unshift(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            node = Node(value, self.head)
            self.head = node

    @push
    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
