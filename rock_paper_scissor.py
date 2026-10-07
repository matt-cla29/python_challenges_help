import random 
opponent_choice = random.choice(["rock", "paper", "scissors"])
play_game = input("would you like to play rock, paper, scissors? (yes/no): ")
while play_game == "yes":
    user_choice = input("user chooose rock, paper, or scissors: ")
    if opponent_choice == "rock" and user_choice == "scissors":
        print("you chose: 🪨")
        print("opponent chose: ✂️")
        print("you lose, rock beats scissors")
    elif opponent_choice == "rock" and user_choice == "paper":
        print("you chose: 📄")
        print("opponent chose: 🪨")
        print("you win, paper beats rock")
    elif opponent_choice == "paper" and user_choice == "scissors":
        print("you chose: ✂️")
        print("opponent chose: 📄")
        print("you win, scissors beats paper")
    elif opponent_choice == "paper" and user_choice == "rock":
        print("you chose: 🪨")
        print("opponent chose: 📄")
        print("you lose, paper beats rock")
    elif opponent_choice == "scissors" and user_choice == "rock":
        print("you chose: 🪨")
        print("opponent chose: ✂️")
        print("you win, rock beats scissors")
    elif opponent_choice == "scissors" and user_choice == "paper":
        print("you chose: 📄")
        print("opponent chose: ✂️")
        print("you lose, scissors beats paper")
    elif opponent_choice == user_choice:
        print("it's a tie")
    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("invalid input, please choose rock, paper, or scissors")
    if play_game == "no":
        print("thank you for playing rock, paper, scissors")
    play_game2 = input("would you like to play again? (yes/no): ")
    if play_game2 == "yes":
        continue
    elif play_game2 == "no":
        print("thank you for playing rock, paper, scissors")
        break