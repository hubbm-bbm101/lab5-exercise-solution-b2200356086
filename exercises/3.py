import random

number=random.randint(1,100)
guess=int(input("Please enter a number"))

while guess!=number:
    if number>guess:
        print("Increase your number")
        guess=int(input("Please enter a number"))
    elif number<guess:
        print("Decrease your number")
        guess = int(input("Please enter a number"))
print("You found!")
