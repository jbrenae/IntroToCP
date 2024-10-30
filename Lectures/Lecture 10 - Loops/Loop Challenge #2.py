# Create a program to print the following table that 
# contains the first four power values for the number 1-10.

for number in range (1,11):
    print("{0:5d} {1:5d} {2:5d} {3:5d}".format(number**1,number**2,number**3,number**4))

print("\nAll done!")