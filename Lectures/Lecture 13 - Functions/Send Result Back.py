def getInput():
    result = 1
    return result

def getInput2():
    result = 1
    quantity = 10
    return result,quantity

def getInput3():
    result = 1

answer = getInput()
print("getInput: ",answer)

answer, amount = getInput2()
print("getInput2: ",answer, amount)

answer = getInput(3)
print("getInput3: ",answer)