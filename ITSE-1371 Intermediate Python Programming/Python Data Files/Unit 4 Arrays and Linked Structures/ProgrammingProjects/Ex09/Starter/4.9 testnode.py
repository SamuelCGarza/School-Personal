"""
File: testnode.py
Project 4.9

Add an insert function.

Tests the Node class.

Reuse your solution from Programming Exercise 4.8 as your starter file
"""

# Reuse your solution from Programming Exercise 4.8 as your starter file
from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    counter = 0
    while head != None:
        head = head.next
        counter += 1
    return counter

def insert(index, newItem, head):
    """Inserts newItem at position is the linked structure
    referred to by head.  Returns a reference to the new
    structure."""
    if index <= 0:
        # newItem goes at the head
        head = Node(newItem, head)
    else:
        # Search for node at position index - 1 or the last position
        probe = head
        while index > 1 and probe.next != None:   
            probe = probe.next;
            index -= 1
        # Insert new node after node at position index - 1 
        # or last position
        probe.next = Node(newItem, probe.next)
    return head

def printStructure(head):
    """Prints the elements in the linked structure."""
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()  # Add a newline to end the line of printed elements



def main():
    """Tests modifications."""
    head = None

    head = insert(0, "1", head)
    print("1:", end = " ")
    printStructure(head)

    head = insert(1, "2", head)
    print("1 2:", end = " ")
    printStructure(head)

    head = insert(0, "0", head)
    print("0 1 2:", end = " ")
    printStructure(head)

    head = insert(3, "3", head)
    print("0 1 2 3:", end = " ")
    printStructure(head)

    head = insert(1, "9", head)
    print("0 9 1 2 3:", end = " ")
    printStructure(head)

if __name__ == "__main__": main()
