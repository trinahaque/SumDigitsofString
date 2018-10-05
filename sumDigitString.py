def sumDigitString(input1, input2=None):
    if input1 == "-f" and input2 != None:
        file = open(input2, "r")
        stringFromFile = file.read()
        result = findSum(stringFromFile)
        file.close()
    elif input1 == "-x" and input2 != None:
        hexInt = int(input2, 16)
        result = findSum(str(hexInt))
    elif isinstance(input1, str):
        result = findSum(input1)
    else:
        return None
    return result
        
def findSum(string):
    sum = 0
    for char in string:
        if char.isdigit() == True:
            sum += int(char)
    return sum

inputFile = "files.txt"
x = sumDigitString("-f", inputFile)
print (x)
