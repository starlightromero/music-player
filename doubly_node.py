"""A Doubly Node within a Linked List."""


class DoublyNode:
    """Create a doubly node."""

    def __init__(self, data):
        """Initialize Node with data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return data and next."""
        return f"Node('{self.prev}', '{self.data}', '{self.next}')"

    def __str__(self):
        """Return data and next."""
        return f"Node('{self.prev}', '{self.data}', '{self.next}')"
