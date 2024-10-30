#
# CGS 2060 - Fall Semester 2024
#
# CGS 2060 Homwork #1 - Owner Surrender Form
#
# Jalisa Greene

print()
print("Please enter owner information")
print()

ownerFirstName = input("First Name: ")
ownerLastName = input("Last Name: ") 
ownerStAddress = input("Street Address: ")
ownerCity = input("City: ") 
ownerState = input("State: " ).upper()

while True:
    if len(ownerState) != 2:
        print("Please re-enter valid state abbreviation")
        ownerState = input("State: " ).upper()
        continue  

    ownerZipCode = input("Zip Code: ") 
   
    if len(ownerZipCode) !=5 or not ownerZipCode or int(ownerZipCode) < 0 or int(ownerZipCode) > 99999:
        print("Please re-enter valid 5-digit zip code!")
        continue
       
    else:
        print(f"{ownerStAddress}, {ownerCity}, {ownerState} {ownerZipCode}")
        print(ownerFirstName, ownerLastName, end="")
        print((40-(len(ownerFirstName)+len(ownerLastName)+1))*" ",end="")
        print(ownerStAddress)
        print(40*" ",end="")
        break
