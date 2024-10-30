# Reading Numbers
# Load input.txt

infile = open("1101 input.txt", "r")

# ---------- Examples ---------- # 

# Integer
line = infile.readline()
print(type(line))

inputNum = int(line)
print(type(inputNum))
print(inputNum)
print(inputNum + 1)
print()

# Float 
line = infile.readline()
print(type(line))

inputNum = float(line)
print(type(inputNum))
print(inputNum)
print(inputNum + 1)
print()