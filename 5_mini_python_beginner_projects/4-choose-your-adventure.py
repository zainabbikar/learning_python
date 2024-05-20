name = input("Type your name: ")
print("Welcome", "to this adventure!")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way do you want to go? " ).lower()

if answer == "left":
    answer = input("You come to a river, you can walk aroud it or swim across? Type walk to walk or swim to swim. ")
    
    if answer == "swim":
        print("You swam across and were eaten by a hippo.")
    elif answer == "walk":
        print("You walked for miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")
        
elif answer == "right":
    answer = input("You come to a bridge, it looks wobble, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you want to talk to them (Yes/No)? ")
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold and you win!!!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose")
    else:
        print("Not a valid option. You lose.")
    
else:
    print("Not a valid option. You lose.")