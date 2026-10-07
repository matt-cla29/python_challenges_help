import random
choice_to_guess = input("would you like to guess a number? (yes/no): ")
while choice_to_guess == "yes":
    between_route = input("which difficulty do you want to try?; \n easy: guess a number between 1 and 10 \n medium: guess a number between 1 and 50 \n hard: guess a number between 1 and 100 \n end: ends the game \n choice: ")
    if between_route == "easy":
        random_number = random.randint(1, 10)
        user_guess = int(input("guess a secret number between 1 and 10: "))
        while user_guess != random_number:
            if user_guess < random_number:
                print("too low")
                user_guess = int(input("guess a secret number between 1 and 10: "))
            elif user_guess > random_number:
                print("too high")
                user_guess = int(input("guess a secret number between 1 and 10: "))
        print("you guessed the correct number!")
    if between_route == "medium":
        random_number = random.randint(1, 50)
        user_guess = int(input("guess a secret number between 1 and 50: "))
        while user_guess != random_number:
            if user_guess < random_number:
                print("too low")
                user_guess = int(input("guess a secret number between 1 and 50: "))
            elif user_guess > random_number:
                print("too high")
                user_guess = int(input("guess a secret number between 1 and 50: "))
        print("you guessed the correct number!")
    if between_route == "hard":
        random_number = random.randint(1, 100)
        user_guess = int(input("guess a secret number between 1 and 100: "))
        while user_guess != random_number:
            if user_guess < random_number:
                print("too low")
                user_guess = int(input("guess a secret number between 1 and 100: "))
            elif user_guess > random_number:
                print("too high")
                user_guess = int(input("guess a secret number between 1 and 100: "))
        print("you guessed the correct number!")
    elif between_route == "end":
            print("thank you for playing the game")
            break


