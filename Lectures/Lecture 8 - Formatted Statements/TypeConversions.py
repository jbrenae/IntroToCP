# Integers - Can easily be counted i.e, 0, 1,2,3,4 or 0, -1,-2,-3,-4
# Float - numbers with decimal point with numbers following i.e, 1.35, 0.3752 (Because the decimal point 'floats' around)

# Numbers with both integers and float will ALWAYS get back a float. 

# -----------------------CONVERSION FUNCTIONS -------------------#
#          type() -- Determine type of number
#          int(7.2)=7 - Drop decimal
#          float(5)=5.0 -Change to decinmal
#          round(3.6)=4 - Round up/down
#          str(17)="17" - Change to string
#          ord() - used to convert a ASCII character to integer
#          chr(number) - converts number to its correspondonding ASCII character


number = 65
fancy = 17.6456
print("3.14 * 2 = ",3.14 *2) #---This is an integer and float used together
print()

print("Determine type of a number: type() = ",type(number))
print("Drop decimal: int() = ",int(fancy))
print("Round up / down: round() = ",round(fancy)) #-- anything 5 and below rounds down 
print("Change to a decimal: float() = ",float(number))
print("Change to string: str() = ",'"'+str(number)+'"')
print("Change to string: str() = ",'"'+str(fancy)+'"')

#implicit type conversion - automatically converys one datwe type to another without any user involvement

x = 10
y = x + 7.3 
print(y)