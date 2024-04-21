"""
Project 5.10
File: arraybag.py
Author: Samuel Garza
"""

from arrays import Array

class ArrayBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self.
        Raises Attribute error if mutation occurs
        within the loop."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def clone(self):
        """Returns a copy of self."""
        return ArrayBag(self)

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """Returns the number of instances of item in self."""
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        # Check if logical size is equal to capacity
        if len(self) == len(self.items):
            
            # Create new array with double the capacity 
            temp = Array(2 * len(self))
            
            # Loop over and copy items in original array to new array
            for i in range(len(self)):
                temp[i] = self.items[i]
                
            # Reassign original array variable to new array     
            self.items = temp
        
        # Place new item at the index value equal to current logical size
        self.items[len(self)] = item
        
        # Increment logical size by 1
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        # If item is not in self raise a KeyError
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        
        # Search for the index of the target item
        # Set search cursor variable
        targetIndex = 0
        
        # Loop over items in array
        for targetItem in self:
            
            # If an item in the array is equal to item argument --> end loop
            if targetItem == item:
                break
            
            # Increment search cursor to move along the array
            targetIndex += 1
            
        # Loop over items from item argument up until the last element 
        for i in range(targetIndex, len(self) - 1):
            
            # Shift items to the left of target up by one position
            self.items[i] = self.items[i + 1]
            
        # Decrement logical size
        self.size -= 1
        
        # Check array memory here and decrease it if necessary
        # If logical size is less than or equal to capacity divided by four,
        # and logical size times two is greater than or equal to default capacity
        if len(self) <= len(self.items) // 4 and \
           2 * len(self) >= ArrayBag.DEFAULT_CAPACITY:
               
            # Create new array with half the capacity
            temp = Array(len(self.items) // 2)
            
            # Loop over and copy items in original array to new array 
            for i in range(len(self)):
                temp[i] = self.items[i]
                
            # Reassign original array variable to new array 
            self.items = temp
       
        
