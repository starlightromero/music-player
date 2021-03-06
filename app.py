"""Import LinkedList class."""
from linked_list import LinkedList
from doubly_linked_list import DoublyLinkedList

data = [
    "The Payback",
    "I Want To Take You Higher",
    "Give Up The Funk",
    "Jungle Boogie",
    "Pick Up the Pieces",
    "Kiss",
]


#                                   LINKED LIST


# Create linked list
ll = LinkedList()

# Append each song in data to linked list
for song in data:
    ll.append(song)

# Print linked list
print("LINKED LIST")
ll.print_list()
print("")

# Prepend "Superfly" and print linked list
print("PREPEND SUPERFLY")
ll.prepend("Superfly")
ll.print_list()
print("")

# Find "Jungle Boogie" and print node
print("FIND JUNGLE BOOGIE")
print(ll.find("Jungle Boogie"))
print("")

# Delete "Jungle Boogie" and print linked list
print("DELETE JUNGLE BOOGIE")
ll.delete("Jungle Boogie")
ll.print_list()
print("")

# Delete head and print linked list
print("DELETE HEAD")
ll.delete_head()
ll.print_list()
print("")

# Delete tail and print linked list
print("DELETE TAIL")
ll.delete_tail()
ll.print_list()
print("")

# Covert linked list to list
print("TO ARRAY")
print(ll.to_array())
print("")

# Reverse linked list
print("REVERSE LINKED LIST")
reverse_ll = ll.reverse()
print(reverse_ll.print_list())
print("")


#                               DOUBLY LINKED LIST


# Create doubly linked list
doubly = DoublyLinkedList()

# Append each song in data to doubly linked list
for song in data:
    doubly.append(song)

# Print doubly linked list
print("DOUBLY LINKED LIST")
doubly.print_list()
print("")

# Prepend "Superfly" and print doubly linked list
print("PREPEND SUPERFLY")
doubly.prepend("Superfly")
doubly.print_list()
print("")

# Find "Jungle Boogie" and print node
print("FIND JUNGLE BOOGIE")
print(doubly.find("Jungle Boogie"))
print("")

# Delete "Jungle Boogie" and print doubly linked list
print("DELETE JUNGLE BOOGIE")
doubly.delete("Jungle Boogie")
doubly.print_list()
print("")

# Delete head and print doubly linked list
print("DELETE HEAD")
doubly.delete_head()
doubly.print_list()
print("")

# Delete tail and print doubly linked list
print("DELETE TAIL")
doubly.delete_tail()
doubly.print_list()
print("")

# Covert doubly linked list to list
print("TO ARRAY")
print(doubly.to_array())
print("")

# Reverse doubly linked list
print("REVERSE DOUBLY LINKED LIST")
reverse_doubly = doubly.reverse()
print(reverse_doubly.print_list())
print("")
