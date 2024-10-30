#Formatted output

name = "John Smith"
televisions = 27

#First Way 

print(" I am "+name+" I own "+str(televisions)+" televisions and I am "+str(4/5)+" of the way through college.")
print()

#Second Way
print(" I am {0} I own {1} televisions and I am {2} of the way through college.")
print()

#Third Way/Flippped

print("I am {1} I own {2} televisions and I am {0} of the way through college.").format((name,televisions,4/5))
print()