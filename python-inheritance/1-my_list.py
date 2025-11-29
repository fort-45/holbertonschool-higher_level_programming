#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""

class MyList(list):
    """A list that has an extra method to print itself sorted."""

    def print_sorted(self):
        """Prints a sorted version of the list (ascending)."""
        print(sorted(self))
