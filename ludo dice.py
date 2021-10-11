# Program to make ludo dice.
import random
val=[1,2,3,4,5,6]
print("Welcom To Ludo Dice")

while (True):
    user=str(input("Enter y for new Number"))
    if (user=="y"):
        result=random.choice(val)
        print("your number " , result)
        continue
    else:
        print("Thank You ")
        print("You Exit The Game")

