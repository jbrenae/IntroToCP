# Follows PEMDAS from grade school. 
# Two exceptions:
    # operations of equal precedence are left associative / Evaluated from left to right

# Example: L---->R

sum = 2+3*4/6
print(sum)
   
   # exponentiation and assignment operations are right associative

# Example: R<----L

sum2 = 3**2**5
print(sum2)

# You can change the order of evaluation by using parenthesis

example = (2+3)*4/5
print(example)