# SET data ( CANT HAVE DUPLICATES )
set_data = {1, 2, 3, "hi"}

set1 = {1, 2, 3}
set2 = {1, 2, 3}

print(set1 == set2)


s1 = {1, 2} <= {1, 2, 3} # checking if subset

print(s1)

# using keyword 'in'

set3 = {1,2,3}

print(1 in set3) # checking if value = 3 is in the set 'set3' It also check the TYPES if they are the same


# LIST data

list_data = [1, 2, 3]
list_names = ['kyle', 'isaac', 'mendoza']


print(list_data + list_names)



# MAPPING data or DICT ( dictionary)
menu_data = {
    'burger': 100.0,
    'fries': 50.0
}


print(menu_data)
print(100.0 in menu_data)

# Key Look up
print(menu_data['burger'])

