"""Linked List which contains many nodes."""
from node import Node


class LinkedList:
    """Linked List class."""

    def __init__(self, head=None, tail=None):
        """Initialize class with head and tail."""
        self.head = head
        self.tail = tail

    def prepend(self, data):
        """Prepend data to linked list."""
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        if self.tail is None:
            self.tail = new_head
