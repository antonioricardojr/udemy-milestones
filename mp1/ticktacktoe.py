# A simple tic tac toe game in python

__author__ = "Antonio Marques"
__version__ = "1.0.0"
__email__ = "antonioricardojr@gmail.com"

BOARD_SIZE = 3
print("Welcome to Tic Tac Toe Game!!!")
print("How to play: insert the line and column you want to mark")

def new_board(size):

	return [["0" for x in range(size)] for y in range(size)]

def print_board(board):

	for line in board:
		print(line)
		
def turn(board, player_on_turn, i, j):

	if i < 0 or j < 0 or i > BOARD_SIZE or j > BOARD_SIZE:
		print("This field does not exist!")
		print("Try again")

	if board[i][j] == "0":
		board[i][j] = player_on_turn
		print("The player {player} at line {line} and column {column}".format(player = player_on_turn, line = i, column = j))
		print_board(board)
		player_on_turn = set_player(player_on_turn)
	else:
		print("The field at line {line} and column {column} was filled already!".format(line = i, column = j))
		print("Try again!")
		print_board(board)
		
	return player_on_turn

def set_player(player_on_turn):
	
	if player_on_turn == "x":
		player_on_turn = "o"
	else:
		player_on_turn = "x"

	return player_on_turn

def has_winner(board):

	for line in board:
		line_set = set(line)
		if len(line_set) == 1 and line_set.pop() != "0":
			return True

	main_diagonal = set([board[0][0] ,board[1][1] ,board[2][2]])
	if len(main_diagonal) == 1 and main_diagonal.pop() != "0":
		return True

	second_diagonal = set([board[2][0], board[1][1], board[0][2]])
	if len(second_diagonal) == 1 and second_diagonal.pop() != "0":
		return True

	for j in range(0, BOARD_SIZE):

		column_set = set([board[0][j], board[1][j], board[2][j]])
		if len(column_set) == 1 and column_set.pop() != "0":
			return True

	return False

def end_game(is_winner):
	if is_winner:
		winner = set_player(player_on_turn)
		print("Congratulations to the player {player}!!").format(player = winner)
		print_board(board)
	exit(0)


board = new_board(BOARD_SIZE)
print_board(board)


player_on_turn = "x"

field = raw_input("line,column: ")
field = field.split(",")
player_on_turn = turn(board, player_on_turn, int(field[0]), int(field[1]))
is_winner = False

while not is_winner:
	field = raw_input("line,column: ")
	field = field.split(",")
	player_on_turn = turn(board, player_on_turn, int(field[0]), int(field[1]))
	is_winner = has_winner(board)

end_game(is_winner)
