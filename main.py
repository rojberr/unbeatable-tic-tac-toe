import random

# Create a list to represent the Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to draw the Tic Tac Toe board
def draw_board():
    print("-------------")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print("-------------")

# Function to check if a player wins
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to make a player's move
def make_move(player, position):
    if board[position] == " ":
        board[position] = player
        return True
    else:
        return False

# Function for the computer's move (random position)
def computer_move():
    available_moves = [i for i, cell in enumerate(board) if cell == " "]
    if available_moves:
        position = random.choice(available_moves)
        board[position] = "O"
        return True
    else:
        return False

# Function to reset the game
def reset_game():
    global board
    board = [" " for _ in range(9)]

# Main game loop
def play_game():
    current_player = "X"
    game_over = False

    while not game_over:
        draw_board()
        if current_player == "X":
            position = int(input("Choose a position (0-8): "))
            if not make_move(current_player, position):
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's turn...")
            if not computer_move():
                print("It's a tie!")
                game_over = True

        if check_win(current_player):
            draw_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif all(cell != " " for cell in board):
            draw_board()
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        reset_game()
        play_game()

if __name__ == '__main__':
    # Start the game
    play_game()