"""Import LinkedList class."""
from linked_list import LinkedList

data = [
    "The Payback",
    "I Want To Take You Higher",
    "Give Up The Funk",
    "Jungle Boogie",
    "Pick Up the Pieces",
    "Kiss",
]


ll = LinkedList()

for song in data:
    ll.append(song)

ll.print_list()
print("")
ll.prepend("Superfly")
ll.print_list()
print("")
print(ll.find("Jungle Boogie"))
print("")
