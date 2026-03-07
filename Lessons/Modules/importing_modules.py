# the import statement
# import <module_name>
import math


# built-in dir function for every other module to see list of functions and other variables defined in the module
# print(dir(math))

for func in dir(math):
    print(help(func))


# datetime module
import datetime 
print(dir(datetime))


for func in dir(datetime):
    print(help(func))