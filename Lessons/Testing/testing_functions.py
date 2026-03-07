# Testing Functions I: doctest and pytest
# Doctests: basic examples in docstrings


def is_even(value: int) -> bool:
    """ Return a boolean wether value is a even
        >>> is_even(2)
        True
        >>> is_even(3)
        False
    """
    return value % 2 == 0




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)