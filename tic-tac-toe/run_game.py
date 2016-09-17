# The next logical step is to deal with handling user input. When a player 
# (say player 1, who is X) wants to place an X on the screen, they can't 
# just click on a terminal. So we are going to approximate this clicking 
# simply by asking the user for a coordinate of where they want to place 
# their piece.
#
# Things to note:
# For this exercise, assume that player 1 (the first player to move) will 
# always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move 
# starting from (1, 1) instead of (0, 0). To people who don't program, 
# starting to count at 0 is a strange concept, so it is better for the user 
# experience if the row counts and column counts start at 1. This is not 
# required, but whichever way you choose to implement this, it should be 
# explained to the player.
# Ask the user to enter coordinates in the form "row,col" - a number, 
# then a comma, then a number. Then you can use your Python skills to figure
# out which row and column they want their piece to be in.
# Don't worry about checking whether someone won the game, but if a player 
# tries to put a piece in a game position where there already is another piece,
# do not allow the piece to go there.

# Bonus:
# For the "standard" exercise, don't worry about "ending" the game - no need
# to keep track of how many squares are full. In a bonus version, keep track
# of how many squares are full and automatically stop asking for moves when
# there are no more valid moves.

import board
import check_using_set

game = [[0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0]]

# Draw game board
board.draw_tic_tac_toe_board(game)
info_msg = 'Please enter coordinates in the form "row,col" - a number, then a comma, then a number.'

player1_char = 'X'
player2_char = 'O'
size = len(game)

print info_msg

count = 0
while True:
    player = 1 if count%2 == 0 else 2
    coordi = raw_input('Player ' + str(player) + ': Please enter the coordinates: ')
    coordi_split = coordi.split(',')
    
    # throw error if, only one digit and comma is entered
    if len(coordi_split) < 2:
        print "Invalid input.", info_msg
        continue
    
    # throw error if, string is added instead of integer
    try:    
        row = int(coordi_split[0])
        col = int(coordi_split[1])
    except:
        print "Invalid input.", info_msg
        continue
    
    # throw error if, row or col is greater than 3 i.e (size - 1)
    if(row > (size - 1) or col > (size - 1)):
        print "Invalid input.", "Coordinates cannot be greater than", str(size - 1)
        continue
    
    # throw error if, the entered coordinates are already occupied
    if(game[row][col] != 0):
        print "Invalid input.", "These coordinates are already filled. Please choose some other coordinates."
        continue
    
    # put X or O in matrix
    game[row][col] = player1_char if player == 1 else player2_char
    count = count + 1
    
    # print game matrix for player reference
    board.draw_tic_tac_toe_board(game)
    
    # check for winner
    winner = check_using_set.check_winner(game, size)
    if winner is not None:
        print "Congratulations! Player " + str(player) + " wins"
        quit()
    elif count == (size * size):
        print "No Winner"
        quit()
