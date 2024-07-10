import math

# Constants for player symbols
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the board
def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

# Function to check if the board is full
def is_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

# Function to evaluate the board for minimax
def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    else:
        return 0

# Minimax function without alpha-beta pruning
def minimax(board, depth, maximizing_player):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    elif is_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using minimax
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, False)
                board[i][j] = EMPTY
                
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    
    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    
    current_player = PLAYER_X
    
    while not is_full(board):
        print_board(board)
        
        if current_player == PLAYER_X:
            print("Player X's turn:")
            x, y = map(int, input("Enter coordinates (row and column): ").split())
            if board[x][y] != EMPTY:
                print("Invalid move! Try again.")
                continue
            board[x][y] = PLAYER_X
        else:
            print("Player O's turn (AI):")
            x, y = find_best_move(board)
            board[x][y] = PLAYER_O
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
    
    if not check_winner(board, PLAYER_X) and not check_winner(board, PLAYER_O):
        print_board(board)
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_game()

