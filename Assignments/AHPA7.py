# If the receipt has a "!" in it
# then it means that this customer # is a high volume customer.

# For each receipt:
# 1. Print out just the name
# 2. Set a Boolean variable if the # customer is a high volume customer
# 3. Print out the Boolean variable
# 4. Print out how much the
# customer spent
# 5. Print out what the customer
# purchased
#
# Student Name: Jalisa Greene
#


totalAmt = 100
customerName = "Bob Johnson"
receipt1 = 127.52
costOfTires = float(127.52)

isHighValue = receipt1 >= totalAmt
output = f"{customerName} ${costOfTires} [Tires]"

if isHighValue:
    output += "!"

print()
print(output)


totalAmt = 100
customerName = "Amy Johnson"
receipt2 = 35.18
oilChange = float(35.18)

isHighValue = receipt2 >= totalAmt
output = f"{customerName} ${oilChange} [Oil Change]"

if isHighValue:
    output += "!"

print()
print(output)


totalAmt = 100
customerName = "Amy Johnson"
receipt3 = 239.15
costOfAlignment = float(239.15)

isHighValue = receipt3 >= totalAmt
output = f"{customerName} ${costOfAlignment} [Oil Change]"

if isHighValue:
    output += "!"

print()
print(output)