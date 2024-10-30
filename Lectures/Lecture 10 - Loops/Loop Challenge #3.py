# Loop Challenge #3

# Temperature: 18.2, 22.6, 26.4,
# 31.1, 36.6, 42.2, 45.7, 44.5
# 40.2, 33.1, 24.2, 17.6

highestTemp = 0
lowestTemp = 1000

for month in range(1,13):
    temp = float(input("Enter temperature: "))
    if (temp > highestTemp):
        highestMonth = month
        highestTemp = temp

    if temp < lowestTemp:
        lowestMonth = month
        lowestTemp = temp

print("Highest Month = ",highestMonth)
print("Highest temp = ",highestTemp)
print("Lowest Month = ",lowestMonth)
print("Lowest temp = ",lowestTemp)
