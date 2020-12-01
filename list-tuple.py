# Convert a list of tuples

list_of_tuple_data = [(3, 4), (7, 8), (100, 200)]

list_data = list(map(list, list_of_tuple_data))

print(list_of_tuple_data)
print(type(list_of_tuple_data[0]))
print(list_data)
print(type(list_data[0]))
