"""A Node within a Linked List."""


class Node:
    """Create a node."""

    def __init__(self, data):
        """Initialize Node with data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return data and next."""
        return f"Node('{self.data}', '{self.next}')"

    def __str__(self):
        """Return data and next."""
        return f"Node('{self.data}', '{self.next}')"
