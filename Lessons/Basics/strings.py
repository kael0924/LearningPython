message = "It\'s a string"

path = r"C:\python\bin" # This is a RAW string ( using the r)

print(message)
print(path)


help_message = '''
  Usage: mysql command
      -h hostname
      -d database name
      -u username
      -p password
'''


print(help_message)


name = 'Kyle'

greetings = f"Good Morning, {name}"
print(greetings)


# CONTATENATION
concat_string = 'This is first string' "This is the second String" # This will only work like this. It doesnt work with variables
print(concat_string)


mood = "fun"
concat_str_using_plus = "This" + "is" + mood # Works even with variables
print(concat_str_using_plus)




# STRINGS ARE ARRAY
fullname = "Kyle Isaac Mendoza"

print(fullname[0:2]) # 0 to 2 (excludes 2)
print(fullname[2:]) # start with index 2 to the last character
print(len(fullname)) # length of the string
