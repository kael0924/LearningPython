def has_more_trues(booleans: list) -> bool:
    """Returns wether boolean list contains more True values than False
        >>> has_more_trues([True, False, True])
        True
        >>> has_more_trues([True, False, False])
        False
    """
    true_counter = 0
    false_counter = 0

    for bool_val in booleans:

        if bool_val:
            true_counter += 1
        else: 
            false_counter += 1

    print(true_counter, false_counter)
    print(true_counter > false_counter)
    return true_counter > false_counter


