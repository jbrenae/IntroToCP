#
#
# 1. Using del: Removes a key-value pair using the key (raises KeyError if the key is not found)

my_dict = {'a': 1, 'b':2}
del my_dict['b']
print(my_dict)

# 2. Using pop(): Removes a key and returns its value (raises KeyError if the key is not found)

my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('b')
print(value)
print(my_dict)

# 3. Using popitem(): Removes and returns the last inserted key-value pair (only for Python 3.7+)

my_dict = {'a': 1, 'b':2}
key, value = my_dict.popitem()
print(key,value)