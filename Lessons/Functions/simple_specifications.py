# Simple Specifications 
def is_even(n: int) -> bool:
    """Return whether n is even.
        >>> is_even(1)
        False
        >>> is_even(2)
        True
    """
    return n % 2 == 0   


# Preconditions in general
# def max_length(strings: set) -> int:
#     """Returns the maximum length of a string in the set of strings.
#         >>> max_length({'Hello', 'Mario', 'David Liu'})
#         9
#     """
#     return max({len(s) for s in strings})

# This will give an error
"""
    >>> empty_set = set()
    >>> max_length(empty_set)
    Traceback (most recent call last):
    File "<input>", line 1, in <module>
    File "<input>", line 7, in max_length
    ValueError: max() arg is an empty sequence
"""

def max_length_sample(strings: set) -> int:
    """Return the maximum length of a string in the set of strings.

    Preconditions:
      - strings != set()
    """
    return max({len(s) for s in strings})


# Preconditions as assumptions and restrictions
def max_length(strings: set) -> int | str:
    """Return the maximum length of a string in the set of strings.

        Return 0 if strings is empty.

        >>> max_length(set())
        0
        >>> max_length({'Kyle', 'Isaac', 'Mendoza'})
        7
    """

    if strings == set():
        return 0
    else:
        return max({len(s) for s in strings})

setA = {
    "Kyle",
    "Isaac",
    "Mendoza"
}

setEmpty = set()

notASet = [1, 2, 3]

# print(max_length(setA)) to Test

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


