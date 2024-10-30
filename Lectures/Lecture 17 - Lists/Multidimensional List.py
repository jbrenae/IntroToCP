#
# List can hold data of mixed type
# 
# List can hold a collection of other lists. 
# 
# Embed the inner list within the enclosing list as needed

multiDim = [[1,2,3],[4,5,6],[7,8,9]]
print(multiDim)

multiDim[2][2] = -1
print(multiDim)

# Understand output

# [[1, 2, 3],       [4, 5, 6],                [7, 8, 9]]
# [[1, 2, 3],       [4, 5, 6],                [7, 8, -1]] 
#      |                 |                          | 
#   List 0            List 1             List 2, 9 is in index 2.
