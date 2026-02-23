# Boolean are TRUE and FALSE

is_active = True
is_admin = False


x = 10 
y = 10

result = x > y 

print(result)


# Comparing strings
str1 = 'a'
str2 = 'b'

str_result = str1 > str2
print(str_result)



# Bool Function
value1 = bool('Hi')
value2 = bool(0)

print(value1, value2)



# Falsy and Truthy values
empty_list = []
empty_str = ''
zero = 0
none_value = None 
empty_tuple = ()
empty_dict = {}

# This are all false
print(bool(empty_list))
print(bool(empty_str))
print(bool(zero))
print(bool(none_value))
print(bool(empty_tuple))
print(bool(empty_dict))
 