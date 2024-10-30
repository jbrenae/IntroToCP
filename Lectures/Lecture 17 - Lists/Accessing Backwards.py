# Backwards

myList = [5, 10, 15, 20, 'a', 'b', 'c']

last = myList[-1]

print("The last element in the list is", last)

print(myList)
for index in range(1,len(myList)+1):
    print(myList[-index]," ",end="")


# This line creates a list called myList containing a mix of integers and strings.
# myList[-1] accesses the last element of the list, which is 'c'.
# The print statement outputs: The last element in the list is c.
# This line prints the entire list: [5, 10, 15, 20, 'a', 'b', 'c'].

# range(1, len(myList) + 1) generates a sequence of numbers from 1 to the length of the list (7 in this case).

# myList[-index] accesses the list elements in reverse order:

# When index is 1, myList[-1] is 'c'.

# When index is 2, myList[-2] is 'b'.

# This continues until index is 7, accessing myList[-7] which is 5.

# print(myList[-index], " ", end="") prints each element followed by a space, without moving to a new line.