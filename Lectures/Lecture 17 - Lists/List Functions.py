

# Common List Functions in Python

# 1. append(x): Adds an item x to the end of the list.

myList = [1, 2, 3]
myList.append(4)
print(myList)  # Output: [1, 2, 3, 4]


# 2. extend(iterable): Extends the list by appending elements from the iterable.

myList = [1, 2, 3]
myList.extend([4, 5])
print(myList)  # Output: [1, 2, 3, 4, 5]


# 3. Insert(i,x) - inserts an x at the given location

myList = [1, 2, 3]
myList.insert(1, 'a')
print(myList)  # Output: [1, 'a', 2, 3]


# 4. Removes the first item from the list whose value is x.

myList = [1, 2, 3, 2]
myList.remove(2)
print(myList)  # Output: [1, 3, 2]


# 5. pop([i]): Removes the item at the given position in the list, 
#    and returns it. If no index is specified, pop() removes and 
#    returns the last item in the list.

myList = [1, 2, 3]
item = myList.pop()
print(item)  # Output: 3
print(myList)  # Output: [1, 2]


# 6. clear(): Removes all items from the list.

myList = [1, 2, 3]
myList.clear()
print(myList)  # Output: []


# 7. index(x[, start[, end]]): Returns the index of the first item whose value is x. 
#    Optional arguments start and end are interpreted as in slice notation.

myList = [1, 2, 3, 2]
idx = myList.index(2)
print(idx)  # Output: 1


# 8. count(x): Returns the number of times x appears in the list.

myList = [1, 2, 3, 2]
cnt = myList.count(2)
print(cnt)  # Output: 2


# 9. sort(key=None, reverse=False): Sorts the items of the list in place (the arguments can be used for sort customization).

myList = [3, 1, 2]
myList.sort()
print(myList)  # Output: [1, 2, 3]


# 10. reverse(): Reverses the elements of the list in place.

myList = [1, 2, 3]
myList.reverse()
print(myList)  # Output: [3, 2, 1]

# 11. copy(): Returns a shallow copy of the list.

myList = [1, 2, 3]
newList = myList.copy()
print(newList)  # Output: [1, 2, 3]
