"""
File: hashset.py
Project 11.5

An hash-based set.
"""

from node import Node
from arrays import Array
from abstractcollection import AbstractCollection
from abstractset import AbstractSet

class HashSet(AbstractSet, AbstractCollection):
    """Represents a hash-based set."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection = None,
                 capacity = None):
        if capacity is None:
            self.capacity = HashSet.DEFAULT_CAPACITY
        else:
            self.capacity = capacity
        self.array = Array(self.capacity)
        self.foundNode = self.priorNode = None
        self.index = -1
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self or False otherwise."""
        self.index = abs(hash(item)) % len(self.array)
        self.priorNode = None
        self.foundNode = self.array[self.index]
        while self.foundNode != None:
            if self.foundNode.data == item: 
                return True
            else:
                self.priorNode = self.foundNode
                self.foundNode = self.foundNode.next
        return False

    def __str__(self):
        """Returns the string representation of self."""
        # Exercise
        result = ""
        for bucket in self.array:
            node = bucket
            while node:
                result += str(node.data) + ", "
                node = node.next
        return "{" + result[:-2] + "}" if result else "{}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        # Exercise
        for bucket in self.array:
            node = bucket
            while node:
                yield node.data
                node = node.next

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.foundNode = self.priorNode = None
        self.index = -1
        self.array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        if not item in self: 
            self.array[self.index] = Node(item,
                                          self.array[self.index])
            self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Exercise 
        if item not in self:
            raise KeyError("Item not in HashSet")
        # Item is in the set; self.foundNode refers to that node
        if self.priorNode is None:
            self.array[self.index] = self.foundNode.next
        else:
            self.priorNode.next = self.foundNode.next
        self.size -= 1
