# http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
# Let's say we want to draw game boards that look like this:
# --- --- --- 
#|   |   |   | 
# --- --- ---  
#|   |   |   | 
# --- --- ---  
#|   |   |   | 
# --- --- ---

def print_horiz_line():
    print ' ---' * board_size
    
def print_vert_line():
    print '{}{}'.format('|','   |' * board_size)

def draw_tic_tac_toe_board(board_size):
    for n in range(0, board_size):
        print_horiz_line()
        print_vert_line()
    print_horiz_line()

if __name__ == "__main__"
    board_size = int(raw_input('What size game board you want?'))
    draw_tic_tac_toe_board(board_size)