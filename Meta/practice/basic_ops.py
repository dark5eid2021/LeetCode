# Append
my_list = [1, 2, 3, 5, 7, 9]
# my_list.append(4)
my_list.remove(1)
print(my_list)

# dictionary
dictionary = {'name': 'Alice', 'age': 25}
# add
dictionary['city'] = 'New York'
# remove
# del dictionary['age']

print(dictionary)
# loop
# for key, value in dictionary.items():
#     print(key, value)


# Tuple
my_tuple=(1, 2, 3)
# tuples are immutable (can't append or modify directly)
print(my_tuple[1]) # 2

# stack
stack = []
stack.append(1)
stack.append(2)

top = stack.pop()
print(stack)

# array
arr = [1, 2, 3]
arr.append(4)
arr.remove(1)

print(arr)