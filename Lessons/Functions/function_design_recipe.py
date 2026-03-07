# Write example uses
# Pick a name for the function (often a verb or verb phrase). Sometimes a good name is a short answer to the question “What does your function do?” Write one or two examples of calls to your function and the expected returned values. Include an example of a standard case (as opposed to a tricky case). Put the examples inside a triple-quoted string that you’ve indented since it will be the beginning of the docstring.

"""
    >> is_even(2)
    >> True
    >> is_even(3)
    >> False
"""


# Write the function header
# Write the function header above the docstring (not indented). Choose a meaningful name for each parameter (often nouns). Include the type contract (the types of the parameters and return value).

# Write the function header


# write the function description
def is_even(value: int) -> bool: # function header
    """ Return wether value is even.

    >> is_even(2)
    >> True
    >> is_even(3)
    >> False
    
    """

    return value % 2 == 0