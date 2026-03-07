import trues



def test_mixture_one_more_trues() -> None:
    """Test has_more_trues on a list with mixture of True and False,
    with one more True than False.
    """
    boolean_list = [True, False, True]
    assert trues.has_more_trues(boolean_list)


def test_mixture_one_more_false() -> None:
    """Test has_more_trues on a list with mixture of True and False,
    with one more False than True
    """
    boolean_list = [False, False, True]
    assert not trues.has_more_trues(boolean_list)

def test_all_true() -> None:
    """Test has_more_trues on a list with all True
    """

    boolean_list = [True, True, True, True]
    assert trues.has_more_trues(boolean_list)

def test_all_false() -> None:
    """Test has_more_trues on a list with all False
    """

    boolean_list = [False, False, False, False, False]
    assert not trues.has_more_trues(boolean_list)




# What is an assert statement
"""So what exactly does an assert statement do? An assert statement has the form assert <expression>, and when one is executed the Python interpreter does the following:

First, it evaluates <expression>, which should produce a boolean value.

If the value is True, nothing else happens, and the program continues onto the next statement.

But if the value is False, an AssertionError is raised. This signals to pytest that the test has failed.
"""


if __name__ == "__main__":
    import pytest
    pytest.main(['test_trues.py'])