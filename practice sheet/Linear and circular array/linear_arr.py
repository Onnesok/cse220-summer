# import numpy as np

# def ar(n, s):
#     idx = 0
#     for i in range(n):
#         if s[i] > 0:
#             if 
#             s[idx] = s[i]
#             idx+=1
    
    
# n = 8
# s =  [1, -1, 3, 2, -7, -5, 11, 6]
# ar(n, s)



import numpy as np

def show_knight_move(knight):
    board = np.zeros((8, 8), dtype=int)
    x, y = knight
    
    # Possible moves of the knight
    moves = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]
    
    for move in moves:
        dx, dy = move
        new_x, new_y = x + dx, y + dy
        
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            board[new_x, new_y] = 3
    
    board[x, y] = 33
    return board


knight = (3,4)
chess_board = show_knight_move(knight)
print_matrix(chess_board)