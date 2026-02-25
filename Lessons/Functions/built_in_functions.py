# Built-in Functions
# <function>(<argument>, <argument>, ...)


# abs() -> absolute
print(abs(-10))


# round() -> given a single argument returns the int that equals x rounded to the nearest integer.
# round(x, d) -> d for decimal 
print(round(3.3))
print(round(-1.678))
print(round(3.456, 2))
print(round(3.456, 0))


# len() -> return the size of its input
list_data = [1, 2, 3 ,10, 20, 1]
set_data = { 1, 3, 5 , 2 , 6}

print(len(list_data))
print(len(set_data))

def say_hello(name=""):
    '''
        This will return the name with appendix string of Hello
    '''
    return f"Hello {name}"

help(say_hello) # can also used on built-in function of python or other libraries


# sum() -> sum function takes a collection of numbers ( e.g., a SET or a LIST that elements is ALL NUMBERS )

print(sum({1, 2, 3, 10, 100}))
print(sum([10, 200, 50, 10, 200]))


# sorted() -> sorted function takes a collection of returns a list that contains the same elements as the input collection. returns a list

print(sorted([1, 5, 3 ,5, 7, 9]))
print(sorted({1, 9, 0 , 2 , 10, 3, 7}))


# max() -> max function is a bit special, because there are two ways it can be used when it is called with two or more inputs, those inputs must be numeric and in this case max returns the LARGEST ONE


print(max(1, 5, 19, 1000, 3)) # returns the largest one
print(max({1, 10, 100, 200, 300}))


# min() -> min function returns the most smallest number

print(min(1, 5, 19, 1000, 3)) # returns the smallest one
print(min({ 10, 100, 200, 300}))


# NOTE you can stack the built-in function
#example
print(type(sum([abs(-1), 4, max(10, 20 ,50), min(10, 30 ,0 )])))