# this function takes a string, a file or a hex value as an input. 
# It returns the sum of the digits in the input.
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

# this function takes a string as an input and returns the sum of the digits in the string.
def findSum(string):
    sum = 0
    for char in string:
        if char.isdigit() == True:
            sum += int(char)
    return sum

# the main calls various function with different test cases
if __name__ == "__main__":
    filename = "files.txt"
    output = sumDigitString("-f", filename)
    print (output)

    output = sumDigitString("-x", "abc123")
    print (output)

    output = sumDigitString("abc123")
    print (output)

    output = sumDigitString("abc")
    print (output)

    output = sumDigitString(123)
    print (output)
