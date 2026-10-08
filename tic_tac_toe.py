# Initialize a blank board with numbers 1-9 as placeholders
board = [str(i) for i in range(1, 10)]

def print_board():
    """Prints the current state of the board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(player):
    """Checks all 8 possible winning combinations."""
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Main Game Loop
current_player = "X"
turns = 0

print("Welcome to Tic-Tac-Toe!")

while turns < 9:
    print_board()
    try:
        choice = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
        
        # Check if the move is valid
        if choice < 0 or choice > 8 or board[choice] in ["X", "O"]:
            print("Invalid move! That spot is either taken or out of bounds. Try again.")
            continue
            
    except ValueError:
        print("Please enter a valid number between 1 and 9.")
        continue

    # Place the player's mark
    board[choice] = current_player
    turns += 1

    # Check for a winner
    if check_win(current_player):
        print_board()
        print(f"🎉 Player {current_player} wins! 🎉")
        break

    # Switch players
    current_player = "O" if current_player == "X" else "X"
else:
    print_board()
    print("🤝 It's a tie! 🤝")
