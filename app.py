from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Create a list to represent the Tic Tac Toe board
board = [" " for _ in range(9)]

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
# Function for the computer's move (random position)
def computer_move():
    available_moves = [i for i, cell in enumerate(board) if cell == " "]
    if available_moves:
        position = random.choice(available_moves)
        board[position] = "O"
        return position
    else:
        return None

# Function to reset the game
def reset_game():
    global board
    board = [" " for _ in range(9)]

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/play', methods=['POST'])
def play():
    position = int(request.form['position'])
    if make_move("X", position):
        if check_win("X"):
            reset_game()
            return jsonify({'status': 'win', 'player': 'X'})
        elif all(cell != " " for cell in board):
            reset_game()
            return jsonify({'status': 'tie'})
        else:
            computer_position = computer_move()
            if computer_position is not None:
                if check_win("O"):
                    reset_game()
                    return jsonify({'status': 'win', 'player': 'O'})
                elif all(cell != " " for cell in board):
                    reset_game()
                    return jsonify({'status': 'tie'})
                else:
                    return jsonify({'status': 'ok', 'position': computer_position})
            else:
                reset_game()
                return jsonify({'status': 'tie'})
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run()
