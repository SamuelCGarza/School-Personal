"""
File: abstractset.py
Project 11.5
"""

class AbstractSet(object):
    """Generic set method implementations."""

    # Accessor methods
    def __or__(self, other):
        """Returns the union of self and other."""
        return self + other

    def __and__(self, other):
        """Returns the intersection of self and other."""
        intersection = type(self)()
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __sub__(self, other):
        """Returns the difference of self and other."""
        difference = type(self)()
        for item in self:
            if not item in other:
                difference.add(item)
        return difference

    def issubset(self, other):
        """Returns True if self is a subset of other
        or False otherwise."""
        for item in self:
            if not item in other:
                return False
        return True

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        # Exercise
        if self is other:  # Check if both are the same object
            return True
        if len(self) != len(other):  # Sets must have the same size
            return False
        for item in self:
            if item not in other:
                return False
        return True

