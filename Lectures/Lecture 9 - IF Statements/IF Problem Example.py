# The variables fieldAmount and fieldCapacity hold the current amount of fuel 
# in a tank and the max size of the fuel tank of a vehicle.

# If less than 10 percent remaining in the tank, a status light should show
# a red color; potherwise, it should show a green color.

# Simulate this process by printing eout either "red" or "green"

        # Step 1:
            #Fuel amount (whats in tank)
            #Average tank is aound 100
                # Will need to divide these to get percentage 


fuelCapacity = 100
fuelAmount = 20

if (fuelAmount / fuelCapacity < 0.1):
    print("red")
else:
    print("green")