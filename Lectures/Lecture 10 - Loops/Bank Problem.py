#
#
# PROBLEM: YOU PUT $10,000 INTO A BANK ACCOUNT THAT EARNS 5 PERCENT INTEREST PER YEAR.
#          HOW MANY YEARS DOES IT TAKE FOR THE ACCOUNT BALANCE TO BE DOUBLE THE ORIGINAL?

# YEAR:                INTEREST                           BALANCE:
#
# 0                                                       $10,000
# 1             10,000 x 0.5 = $500.00       $10,000 + $500.00 = $10,500.00
# 2             10,500 x 0.5 = $525.00       $10,500.00 + $525.00 = $11,025.00
# 3             11,025.00 x 0.5 = $551.25    $11,025.00 + $551.25 = $11,576.25
# 4             11,576.25 x 0.5 = $578.81    $11,576.25 + $578.81 = $12,155.06   

accountAmount = 10000
interestRate = 0.05
double = accountAmount * 2
numYears = 0

while(accountAmount < double):
    interestEarned = accountAmount * interestRate
    accountAmount = accountAmount + interestEarned
    numYears += 1

print("Amount in checking account = {0:,.2f}".format(accountAmount))
print("Number of years required = ",numYears)

        