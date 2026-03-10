LOVES_TABLE = [
    [False, True, True, False],
    [False, True, True, True],
    [False, False, True, False],
    [False, False, True, True]
]

A = {
    'Breana': 0,
    'Melena': 1,
    'Patrick': 2,
    'Ella': 3
}

B = {
    'Sophia': 0,
    'Thelonious': 1,
    'Stanly': 2,
    'Laura': 3,
}



def loves(a: str, b: str) -> bool: 
    """Return weather a person a loves person b
        Assuming that:
        - a in A
        - b in B

        >>> loves('Breana', 'Sophia')
        False
    """
    a_index = A[a]
    b_index = B[b]  
    return LOVES_TABLE[a_index][b_index]


print(all({loves(a,b) for a in A for b in B}))
print(any({loves(a,b) for a in A for b in B}))

print(all(any({loves(a,b) for b in B}) for a in A))

def loves_someone(a: str) -> bool:
    """Return wether a loves at least one person in B.

        Assuming that:
        - a in A
    """ 
    return any({loves(a,b) for b in B})


print(all({loves_someone(a) for a in A}))


def loved_by_everyone(b: str) -> bool:
    """Return whether b is loved by everyone in A.

    Assuming that:
      - b in B
    """
    return all({loves(a, b)} for a in A)



# TO TEST
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)