'''
HW : Q1.explain all the methods on set with code 
     Q2. we can add set into list and tuple? check through program
'''
# Q1. explain all the methods on set with code
# creating a set
my_set = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Original set:", my_set)

original_list = [12, 3+5j, 2, True, 'Sai']
print("\nOriginal list:", original_list)

original_list.append(my_set)
print("Inserting set into list:", original_list)

# we can add set into list but we cannot add set into tuple because tuple is immutable
my_tuple = (1, 2, 3)
print("\nOriginal tuple:", my_tuple)
# my_tuple.append(my_set) # this will give an error because tuple is immutable

# to add a set into a tuple we can convert the tuple into a list and then add the set and then convert it back to a tuple
my_tuple = list(my_tuple)
my_tuple.append(my_set)
my_tuple = tuple(my_tuple)
print("Inserting set into tuple by converting into list",my_tuple)

# print(my_set-set2) # {1, 2, 3}  # reason: it will give the elements which are present in my_set but not in set2
