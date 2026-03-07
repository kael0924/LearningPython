

def example_def(a: str, b: str):
    """This is just an example
    """
    return a + b



# DONT DO THIS unless you want to run the whole doctest every import of the main_block.py file
import doctest # DONT DO THIS
doctest.testmod() # DONT DO THIS


# TO RUN This solely if the current file is running use the if and __name__ block

if __name__ == "__main__":
    import doctest 
    doctest.testmod()