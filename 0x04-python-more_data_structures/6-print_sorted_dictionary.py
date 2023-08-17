#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Returns a set of all elements present in only one set
    ...
    Parameters
    ----------
    set_1 : set
    first set of elements
    set_2 : set
    second set of elements
    Return:
    the result of the operation (&)
    """

    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
