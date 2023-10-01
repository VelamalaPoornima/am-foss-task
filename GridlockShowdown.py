def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][i] == board[i][2] and board[i][0] != '.':
            return board[i][0]
        
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]
    
    return "DRAW"

t = int(input())
for i in range(t):
    board = [list(input()) for j in range(3)]
    winner = check_winner(board)
    print(winner)
