def is_safe_move(board,row,col,N):
    return 0 <= row < N and 0<=col<N and board[row][col] == -1

def  print_board(board,N):
    for row in board:
        print("/t".join(str,row))
    
def knight_tour(board,row,col,moves_count,N,row_moves,col_moves):
    if moves_count == N*N:
        return True
    
    for i in range(8):
        next_row = row + row_moves[i]
        next_col = col + col_moves[i]
        
    if is_safe_move(board,next_row,next_col,N):
        board[next_row][next_col] = moves_count
        
    if knight_tour(board,next_row,next_col,moves_count+1,N,row_moves,col_moves):
        return True
        board[next_row][next_col] = -1
        
    return False      
          