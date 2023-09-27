# Author: Xander Wang
# Date: 2023-9-25
print()
print("define the list of strings of any five fruits")
fruit_list = ["strawberry", "blueberry", "watermelon", "pineapple", "pear"]

# Print the whole list
print(fruit_list)
print()

# Print one list item at a time
for x in fruit_list:
    print(x)
print()

# Print one list item at a time using indices
for i in range(len(fruit_list)):
    print(fruit_list[i])
print()

# Add another item to list
fruit_list.append("banana")
print(fruit_list)
print()

# Remove second item from list
fruit_list.remove("blueberry")
print(fruit_list)
print()

# Print size of list
print(len(fruit_list))
print()

# Clear the list
fruit_list.clear()
print(fruit_list)