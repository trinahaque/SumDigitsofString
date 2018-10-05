# SumDigitsofString

## Installation and Set Up
This project is built using Python 3.5.2. Download Python 3 from https://www.python.org/downloads/ if it's not already installed in the machine. 
More details about Python 3 installation and Setup can be found [here](https://realpython.com/installing-python/)

## Running The Project
After Python 3 is installed, follow the instructions below to run the project:
1. Clone the git repository in the local machine.
2. Navigate to the project directory. It will look similar to this
```
__pycache__		sumDigitString.py
files.txt		  unitTest.py
```
3. Type the command below to run the file:
```
python3 sumDigitString.py
```
4. Type the command below to run the test file:
```
python3 unitTest.py
```

## Assumptions and Instructions
To run the `sumDigitString.py` file with other inputs, call the function in the main and pass inputs accordingly. Wrap it inside `print ()` to print the output in the console
1. If it's a string input, type in the string wrapped inside a quote as an input. Example below:
`print (sumDigitString("abc123"))`
2. If it's a file input, type in "-f" as the first input, the location of the file inside a quote as the second input. Example below:
`print (sumDigitString("-f", "fileLocation"))`
3. If it's a hex input, type in "-x" as the first input, the hex string inside a quote as the second input. Example below:
`print (sumDigitString("-x", "abc123"))`
