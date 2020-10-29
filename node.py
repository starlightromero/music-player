"""A Node within a Linked List."""


class Node:
    """Create a node."""

    def __init__(self, data, next_node=None):
        """Initialize Node with data."""
        self.data = data
        self.next = next_node

    def __repr__(self):
        """Return data and next."""
        return f"Node(Song: '{self.data}')"

    def __str__(self):
        """Return data and next."""
        return f"Node(Song: '{self.data}')"
