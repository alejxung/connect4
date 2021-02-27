import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT)) # 6 rows 7 columns init state
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0 # Checking top row whether there is a piece

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals for win
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals for win
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1, Make your selection 0~6\n=> "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 Wins!")
                game_over = True

    # Ask for Player 2 Input
    else:
        col = int(input("Player 2, Make your selection 0~6\n=> "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("Player 2 Wins!")
                game_over = True
    
    turn += 1
    turn %= 2

    print_board(board)