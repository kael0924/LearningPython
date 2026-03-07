def square(x: float) -> float: # this is a function header, -> float meaning the return type is a float
    '''
        return x squared.

        Example:
        >>> square(3.0)
        9.0
    '''
    # This is the function body
    return x ** 2 # 


# Syntax for a function header for unary function is:
# def <function_name>(parameter_name: parameter_type) -> return_type:

# using the function
number = int(input("Input number to know its square root: "))
print(f"Square root of {square(number)}")


# Using help() built-in function in custom function
help(square)



#
def calculate_distance(p1: list, p2: list) -> float:
    """
        Returns the distance between point 1 and point 2

        p1 and p2 are list of the form [x,y] where the x- and y y-coo

        >>> calculate_distance([0,0], [3.00, 4.0])
        5.0
    """
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    return (square(x2 - x1) + square(y2 - y1)) ** .5


print(calculate_distance([0,0], [3.0, 4.0]))

