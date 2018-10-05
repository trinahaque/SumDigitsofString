# This function takes a string, a file or a hex value as an input
# "-f" in input1 specifies that the input2 will contain a file with string in it
# "-x" in input1 specifies that the input2 will contain a hex string
# Only 1 input specifies that the input is just a string. input2's default value will be none
# It returns the sum of the digits in the string
# It returns None if an invalid input is entered
def sumDigitString(input1, input2=None):
    # checks if the input is a file
    if input1 == "-f" and input2 != None:
        file = open(input2, "r")
        stringFromFile = file.read()
        result = findSum(stringFromFile)
        file.close()
    # checks if the input is a hexstring
    elif input1 == "-x" and input2 != None:
        # hexInt converts the input hex string to an int
        hexInt = int(input2, 16)
        result = findSum(str(hexInt))
    # checks if the input is a string
    elif isinstance(input1, str):
        result = findSum(input1)
    # checks for all invalid input. Returns None in that case
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
    # running the function with two inputs.  "-f" in input 1 it's a file input and "files.txt" in input2 has a file with string in it
    print (sumDigitString("-f", "files.txt"))
    # running the function with two inputs. "-x" in input 1 specifies it's a hex string, input2 is a hex string
    print (sumDigitString("-x", "abc123"))
    # running the function with one input that is string with digits in it
    print (sumDigitString("abc123"))
    # running the function with one input that is string without digits in it
    print (sumDigitString("abc"))
    # running the function with one with invalid input
    print (sumDigitString(123))
