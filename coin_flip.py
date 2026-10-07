import random
coin_flip = input("would you like to flip a coin? (yes/no): ")
while coin_flip == "yes":
    flipping_coin = random.choice(["heads", "tails"])
    print("the coin has landed on", flipping_coin)
    if coin_flip == "no":
        print("thank you for flipping a coin")
    coin_flip2 = input("would you like to flip another coin? (yes/no): ")
    if coin_flip2 == "yes":
        continue
    elif coin_flip2 == "no":
        print("thank you for flipping a coin")
        break
