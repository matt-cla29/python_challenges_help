import random
choice_to_roll = input("would you like to roll the dice? (yes/no): ")
while choice_to_roll == "yes":
    dice_roll = random.randint(1, 6)
    print("you rolled a", dice_roll)
    if choice_to_roll == "no":
        print("thank you for rolling the dice")
    choice_to_roll2 = input("would you like to roll the dice again? (yes/no): ")
    if choice_to_roll2 == "yes":
        continue
    elif choice_to_roll2 == "no":
        print("thank you for rolling the dice")
        break
