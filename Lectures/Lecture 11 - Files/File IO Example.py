# File IO Example
# Load numbers.txt

infile = open("1105 numbers.txt", "r")
outfile = open("1105 foratted.txt", "w")

total = 0
numNumbers = 0

number = infile.readline()

while (number != ""):               #<----- In the expression `number != ""`, the 
                                        # exclamation mark (`!`) is used as a logical NOT operator in some 
                                        # programming languages, but in this context, it’s part of the inequality operator `!=`, 
                                        # which means "not equal to." So, `number != ""` checks whether `number` 
                                        # is not equal to an empty string. The loop continues as long as `number` contains something
                                        #  (i.e., it’s not empty).
    number = float(number)
    print("{0:15.2f}".format(number),file=outfile)
    total += number
    numNumbers += 1
    number = infile.readline()

print("-"*15,file=outfile)
print("Total: {0:6.2f}".format(total),file=outfile)
print("Average: {0:6.2f}".format(total/numNumbers),file=outfile)

infile.close()
outfile.close()
print("All Done!")