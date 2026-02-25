# Set Comprehensions
numbers = { 1, 2, 3, 4, 5}

# { <expressions> for <variable> in <collection> }



numbers_comprehensions = {x ** 2 for x in numbers }
print(f"Set Comprehension Results {numbers_comprehensions}")


numbers_comprehensions_with_list = {x ** 2 for x in [1,2,3,4,5] }
print(f"Set Comprehension with List Result {numbers_comprehensions_with_list}")



# List and Dictionary Comprehensions
list_and_dictionary_comprehensions_result = [ x + 4 for x in {10, 20, 30}] # This is unordered 
list_and_list_comprehensions_result = [ x + 4 for x in [10,20,30 ]]

print(f"Set Comprehension with List and Dictionary {list_and_dictionary_comprehensions_result}")
print(f"Set Comprehension with List and List {list_and_list_comprehensions_result}")



# Dictionary Comprehensions
# { key-expr: value-expr for <variable> in <collection> }
dictionary_comprehension_result = { f"key-{x}": f"value-{x}" for x in numbers}

print(dictionary_comprehension_result)


# Tuples Comprehensions
# Mostly used in cartesians product
x_set = {1, 2, 3}
y_set = {10, 20, 30}
tuples_comprehension_result = { (x, y) for x in x_set for y in y_set }

print(f"Tuples Comprehension Result {tuples_comprehension_result}")
