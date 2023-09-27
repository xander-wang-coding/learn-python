# Author: Xander Wang
# Date: 2023-9-24
 
# The clear() method
print("clear() method")
this_list = ["apple", "banana", "cherry"]
print(this_list)
this_list.clear()
print(this_list)
print()

# Loop through a list
print("Loop through a list")
this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)
print()

# The range() function
print("The range() function")
x = range(6)
print(type(x))
print(x)
for n in x:
    print(n)

print()
x = range(5, 20, 4)
for n in x:
    print(n)

# Loop through Index #'s
print()
print("Loop through Index #'s")
for i in range(len(this_list)):
    print(this_list[i])

