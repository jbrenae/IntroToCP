
thermostatTemperature = 0

if outsideTemp < 70 : 
    thermostatTemperature = 85
    firePlace = 1
    hotChocolate = 1
    print("The room will be heated")
else:
    thermostatTemperature = 78
    print("The room will be cooled")

