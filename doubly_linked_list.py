"""Doubly Linked List which contains many nodes."""
from linked_list import LinkedList
from doubly_node import DoublyNode


class DoublyLinkedList(LinkedList):
    """Doubly Linked List class."""

    def prepend(self, data):
        """Prepend data to doubly linked list."""
        new_head = DoublyNode(data, None, self.head)
        self.head = new_head
        if self.tail is None:
            self.tail = new_head
            self.tail.prev = self.head

    def append(self, data):
        """Append data to doubly linked list."""
        new_tail = DoublyNode(data)
        if self.tail:
            new_tail.prev = self.tail
            self.tail.next = new_tail
        elif self.head:
            new_tail.prev = self.head
            self.head.next = new_tail
        self.tail = new_tail
        if self.head is None:
            self.head = new_tail

    def delete(self, data):
        """Delete node with given data."""
        if self.head is None:
            return None
        while self.head and self.head.data == data:
            self.head = self.head.next
        cur_node = self.head
        while cur_node.next:
            if cur_node.next.data == data:
                cur_node.next.next.prev = cur_node
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next

    def delete_head(self):
        """Delete head of doubly linked list."""
        if self.head is None:
            return None
        deleted_node = self.head
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
        return deleted_node

    def delete_tail(self):
        """Delete tail of doubly linked list."""
        if self.tail is None:
            return None
        deleted_node = self.tail
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        return deleted_node
