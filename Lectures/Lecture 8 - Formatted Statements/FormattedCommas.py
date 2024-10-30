## Printing commas that seperate the thousands.

monthlyCost = 428
purchasePrice = 33550.00

print("Cost = ${0:.2f} ${1:5.2f}".format(monthlyCost,purchasePrice))

## Placing a comma in your output number to the print formatting statement

print("Cost = ${0:,.2f} ${1:5,.2f}".format(monthlyCost,purchasePrice))
