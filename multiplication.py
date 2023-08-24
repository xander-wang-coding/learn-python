x = input("Do you want to learn some math?")
if x == "yes":
   print("Good choice")
   y = input("Type the first number: ")
   z = input("Type the second number: ")
   print("The answer to your multiplication question is: ")
   print(int(y) * int(z))
else:
   print("Are you sure about that?")