# This script check the pointer of int / dict 

# For dictionary 

dict1 = { 'value':11 }
dict2 = dict1 

# Before  Modification 
print('Before modification')
print('\n dict1 points to ',id(dict1))
print('dict2 points to ',id(dict2))

print("Is dict2 points to dict1 memory location?", id(dict1) == id(dict2))


# Change the values 
dict2['value'] = 22 

print("After changeing value, is dict2 points to dict1 memory location?", id(dict1) == id(dict2))


dict3 = {'value': 33}
dict2 = dict3 
dict1 = dict2

# After Modification 
print('After modification')
print('\n dict1 points to ',id(dict1))
print('dict2 points to ',id(dict2))
print('dict3 points to ',id(dict3))