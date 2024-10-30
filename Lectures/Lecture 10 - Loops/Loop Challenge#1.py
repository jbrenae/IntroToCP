# Creat a program program to proint the sum 
# of all off numbers between a and b
# (inclusive) using a for loop



a = int(input("Enter a: "))
b = int(input("Enter b: "))

sum = 0

if (a%2 ==0):
    for number in range(a+1,b+1,2):
        sum += number
else:
    for number in range(a,b+1,2):
        sum += number

print("Sum is ",sum)