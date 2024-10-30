#When operators share an operand, the operator with the higher precedence goes first
    # a + b * c  is treated as a a+(b*c) and a * b + c is treated as (a * b) + c.

#Associativity: when operators share same operand and same precedence, then the expression is evaluated
#   according to the associativity of ther operators.
    #       a ** (b ** c) is treated as a ** (b**c)-- the ** operator has right to left associativity 
    #       a / b / c is terated as (a/b) / c -- the "/" operator has left-to-right associativuty

#Order of evaulation: The LEFT operand is always evaulated before the right operand

#-----------------------------------------------------------------------------------------------------------------#

print(2 + 3 * 3) #is 11 or 15?
print( 16 / 4 / 2) #is 8 or 2?