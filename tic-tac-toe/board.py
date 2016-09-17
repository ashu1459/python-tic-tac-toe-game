# http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
# Let's say we want to draw game boards that look like this:
# --- --- --- 
#|   |   |   | 
# --- --- ---  
#|   |   |   | 
# --- --- ---  
#|   |   |   | 
# --- --- ---

def print_horiz_line(game_matrix_row):
    print ' ---' * len(game_matrix_row)
    
def print_vert_line(game_matrix_row):
    if(game_matrix_row is None):
        print '{}{}'.format('|','   |' * len(game_matrix_row))
    else:
        line = '|'
        for num in game_matrix_row:
            filling = ' ' if num == 0 else num
            line = line + ' ' + filling + ' |'
        print line
        
def draw_tic_tac_toe_board(game_matrix):
    for n in range(0, len(game_matrix)):
        print_horiz_line(game_matrix[n])
        print_vert_line(game_matrix[n])
    print_horiz_line(game_matrix)
