import random
print("Welcome,Lets roll the dice")
x = "y"
while x == "y":
    z = random.randint(1, 6)
    if z == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    if z == 2:
        print("---------")
        print("|       |")
        print("|   00  |")
        print("|       |")
        print("---------")
    if z == 3:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|   0   |")
        print("---------")
    if z == 4:
        print("---------")
        print("|   0   |")
        print("|  0 0  |")
        print("|   0   |")
        print("---------")
    if z == 5:
        print("---------")
        print("|   0   |")
        print("| 0 0 0 |")
        print("|   0   |")
        print("---------")
    if z == 6:
        print("---------")
        print("|     00|")
        print("|   00  |")
        print("| 00    |")
        print("---------")
    x = input("Do you want to roll dice again(y/n) :")
