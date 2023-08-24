# Author: Xander Wang
# Date: 2023 - 8 - 23

# This script is a calculator.

print("Please select only one operation you want to do: +, -, *, or /")
operation = input()
print("Please specify the first number: ")
x = float(input())
print("Please specify the second number: ")
y = float(input())

# control logic
if operation == '+':
    z = x + y
elif operation == '-':
    z = x - y
elif operation == '*':
    z = x * y
elif operation == '/':
    z = x / y
else:
    exit('Unknown operation!')

print(z)