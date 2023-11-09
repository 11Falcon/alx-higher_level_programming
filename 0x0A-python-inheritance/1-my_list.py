#!/usr/bin/python3
"""
 class MyList that inherits from list
 Public instance method: def print_sorted(self):
  prints the list, but sorted (ascending sort)
  """


class MyList(list):
    """
    MyList inherits from list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        print the list sorted ascending
        """
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))

