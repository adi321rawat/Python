#from __future__ import print_function
import random
board = [' '] * 10
def display_board(b):
	print ('   |   |')
	print (' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print ('   |   |')
	print ('----------')
	print ('   |   |')
	print (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print ('   |   |')
	print ('----------')
	print ('   |   |')
	print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print ('   |   |')
	
def player_input(): 
        marker = ' '    
	while not (marker == 'X' or marker == 'O'):
		marker = raw_input("Enter the marker (X or O): ").upper()
	if marker == 'X':
		return('X','O')
	else: 
		return ('O','X')

def place_marker(board,marker,position):
        board[position] = marker
        
def win_check(board,mark):
	return ((board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark))
        
def choose_first():     
       	if random.randint(0,2) == 0:
		print ("Player 1 goes first!!")
		return 'player1'
	else:
		print ("Player 2 goes first!!")
                return 'player2'
        
def space_check(board,position):
        return board[position] == ' '

def full_board_check(board):
        for i in range(1,10):
		if space_check(board,i):
			return False
	return True

def player_choice(board):
        position = ' '
        while position not in '1 2 3 4 5 6 7 8 9'.split(' ') or not space_check(board,int(position)):
                position = raw_input("Enter position: ")
        return int(position)
                	
def replay():
        return raw_input("Wanna Play Again????(Yes|No): ").lower().startswith('y')
     
print ("Welcome to Tic-Tac-Toe!")
while True:
        game = True
        player1_marker,player2_marker = player_input()
        turn = choose_first()
        while game:
                if turn == 'player1':
                        display_board(board)
                        position = player_choice(board)
                        place_marker(board,player1_marker,position)
                        if win_check(board,player1_marker):
                                display_board(board)
                                print ("Congrats! Player1 won!!")
                                game = False
                        else:
                                if full_board_check(board):
                                        display_board(board)
                                        print ("It's a Draw.")
                                else:
                                        turn = 'player2'
                else:
                        display_board(board)
                        position = player_choice(board)
                        place_marker(board,player2_marker,position)
                        if win_check(board,player2_marker):
                                display_board(board)
                                print ("Congrats! Player2 won!!")
                                game = False
                        else:
                                if full_board_check(board):
                                        display_board(board)
                                        print ("It's a Draw.")
                                else:
                                        turn = 'player1' 
        if not replay():
                break                
        
