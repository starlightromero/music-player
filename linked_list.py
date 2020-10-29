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

    def append(self, data):
        """Append data to linked list."""
        new_tail = Node(data)
        new_tail.next = None
        if self.tail:
            self.tail.next = new_tail
        self.tail = new_tail
        if self.head is None:
            self.head = new_tail

    def delete_head(self):
        """Delete head of linked list."""
        if self.head is None:
            return None
        deleted_node = self.head
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        return deleted_node

    def delete_tail(self):
        """Delete tail of linked list."""
        if self.tail is None:
            return None
        deleted_node = self.tail
        cur_node = self.head
        while cur_node.next:
            if cur_node.next == self.tail:
                cur_node.next = None
                self.tail = cur_node
            else:
                cur_node = cur_node.next
        return deleted_node
