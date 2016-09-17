# checking whether someone has WON a game of Tic Tac Toe, not worrying about 
# how the moves were made.

game = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
#game = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
#game = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
#game = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
#game = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
#game = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]
#game = [[1, 1, 0], [2, 2, 2], [2, 1, 0]]
#game = [[0, 1, 0], [2, 1, 2], [2, 1, 0]]

def check_horizontal(game, size):
    for r in range(size):
        if game[r][0] == game[r][1] == game[r][2] != 0:
            return game[r][0]
            
def check_vertical(game, size):
    for r in range(size):
        if game[0][r] == game[1][r] == game[2][r] != 0:
            return game[0][r]

def check_diagonal(game, size):
    diagonal1 = []
    diagonal2 = []
    
    for r in range(size):
        diagonal1.append(game[r][r])
        diagonal2.append(game[r][(size - 1) - r])

    if len(set(diagonal1)) == 1 and diagonal1[0] != 0:
        return diagonal1[0]
    elif len(set(diagonal2)) == 1 and diagonal2[0] != 0:
        return diagonal2[0]

def check_winner(game, size):
    ch = check_horizontal(game, size)
    if ch is not None: return ch
    
    cv = check_vertical(game, size)
    if cv is not None: return cv
    
    cd = check_diagonal(game, size)
    if cd is not None: return cd

if __name__ == '__main__':
    winner = check_winner(game, len(game))
    print "No Winner" if winner is None else "Player " + str(winner) + " wins"
