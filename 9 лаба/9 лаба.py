import tkinter as tk

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def computer_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        row, col = move
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state=tk.DISABLED)
        if check_winner(board, 'O'):
            result_label.config(text="Компьютер выиграл!")
            disable_all_buttons()
        elif is_full(board):
            result_label.config(text="Ничья!")
            disable_all_buttons()

def player_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED)
        if check_winner(board, 'X'):
            result_label.config(text="Игрок выиграл!")
            disable_all_buttons()
        elif is_full(board):
            result_label.config(text="Ничья!")
            disable_all_buttons()
        else:
            computer_move()

def disable_all_buttons():
    for row in buttons:
        for button in row:
            button.config(state=tk.DISABLED)

def reset_game():
    global board, buttons
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for button in row:
            button.config(text='', state=tk.NORMAL)
    result_label.config(text="")

root = tk.Tk()
root.title("Крестики-нолики")

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        button = tk.Button(root, text='', width=10, height=3, font=('Arial', 24),
                           command=lambda i=i, j=j: player_move(i, j))
        button.grid(row=i, column=j)
        buttons[i][j] = button

result_label = tk.Label(root, text="", font=('Arial', 16))
result_label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Сброс", font=('Arial', 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
