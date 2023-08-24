# Author: Xander Wang
# Date: 2023-08-23

# This script takes in a number and calculates its factorial.

import math

print("Please enter number for factorial")
x = int(input())

z = math.factorial(x)

print('The factorial of ' + str(x) + " = " + str(z))