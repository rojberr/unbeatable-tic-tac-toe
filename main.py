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
def random_computer_move():
    available_moves = [i for i, cell in enumerate(board) if cell == " "]
    if available_moves:
        position = random.choice(available_moves)
        board[position] = "O"
        return True
    else:
        return False

# Minimax algorithm for the AI player
def minimax(player):
    # Base cases: check if the game is over
    if check_win("X"):
        return -1
    elif check_win("O"):
        return 1
    elif all(cell != " " for cell in board):
        return 0

    # List to hold the scores of each possible move
    scores = []

    # Iterate over available moves
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if player == "O":
                result = minimax("X")
                scores.append(result)
            else:
                result = minimax("O")
                scores.append(result)
            board[i] = " "  # Undo the move

    # Calculate the best score based on the current player
    if player == "O":
        best_score = max(scores)
    else:
        best_score = min(scores)

    return best_score

# Function for the AI's move (best possible move using minimax)
def ai_move():
    available_moves = [i for i, cell in enumerate(board) if cell == " "]
    if available_moves:
        best_score = float('-inf')
        best_move = None

        # Iterate over available moves and calculate scores
        for move in available_moves:
            board[move] = "O"
            score = minimax("X")
            board[move] = " "  # Undo the move

            # Update the best score and move
            if score > best_score:
                best_score = score
                best_move = move

        board[best_move] = "O"
        return True
    else:
        return False

# Function to reset the game
def reset_game():
    global board
    board = [" " for _ in range(9)]

# Main game loop
def play_game():
    player_mode = input("Choose player mode:\n1. Random Computer\n2. AI Computer\n")
    if player_mode == "1":
        player_turn = "X"
        computer_turn = "O"
        computer_move_fn = random_computer_move
    elif player_mode == "2":
        player_turn = "X"
        computer_turn = "O"
        computer_move_fn = ai_move
    else:
        print("Invalid input. Try again.")
        play_game()

    current_player = player_turn
    game_over = False

    while not game_over:
        draw_board()
        if current_player == player_turn:
            position = int(input("Choose a position (0-8): "))
            if not make_move(current_player, position):
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's turn...")
            if not computer_move_fn():
                print("It's a tie!")
                game_over = True

        if check_win(current_player):
            draw_board()
            if current_player == player_turn:
                print("You win!")
            else:
                print("Computer wins!")
            game_over = True
        elif all(cell != " " for cell in board):
            draw_board()
            print("It's a tie!")
            game_over = True
        else:
            current_player = player_turn if current_player == computer_turn else computer_turn

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        reset_game()
        play_game()

if __name__ == '__main__':
    # Start the game
    play_game()