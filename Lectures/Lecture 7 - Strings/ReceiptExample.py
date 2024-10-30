# Customer Receipt Example

firstName = "First"
lastName = "Last"
streetAddress = "Street"
city = "City"
state = "ST"
zipCode = "12345"

print()

print(firstName, lastName, end="")
print((40-(len(firstName)+len(lastName)+1))*" ",end="")
print(streetAddress)
print(40*" ",end="")
print(city,state,zipCode)
