# AHPA #8 - The UPC Code

# Student Name: Jalisa Greene


#Part 1: 

#Your assignment is to take a UPC code, divide it up into its four parts, 
# then print them out in separate fields on a single line. 

#Use this UPC code:
#(020357122682)

#Note: the program has to work for ANY UPC code in this formatâ€¦


upc_code = "020357122682"
part1 = upc_code[0]
manufactCode = upc_code[1:6]
productCode = upc_code[6:11]
checkDigit = upc_code [11]

print()
print("UPC: " +(part1)+ " " +(manufactCode)+ " " +(productCode)+ " " +(checkDigit)+ " ")


unitPrice = 275.15
quantityOfItem = 12
totalPrice = unitPrice * quantityOfItem

print(f"Price: ${unitPrice} Qty: {quantityOfItem} Total Price: ${totalPrice:7,.2f}")