from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

import random
import sys
import copy


class RequestHandler(SimpleXMLRPCRequestHandler):
	    rpc_paths = ('/tic-tac-toe',)


games = {}

def new_game():
    game_id = randint(0, 9999999)

    # To be sure unique game_id accross games
    while game_id in games:
        game_id = randint(0, 9999999)

    # Creating initial board
    board = []
    for i in range(9):
        board.append(-1)
    games[game_id] = board

    return game_id


def new_move(game_id, index):
    board = games[game_id]
    board[index] = 1
    ai_move_index = _new_ai_move_index(copy.deepcopy(board))
    if ai_move_index != None:
		board[ai_move_index] = 0
    games[game_id] = board
    return board

def _new_ai_move_index(board):

    # check if bot can win in the next move
    for i in range(0,len(board)):
        board_copy = copy.deepcopy(board)
        if _is_move_valid(board_copy, i):
			board_copy[i] = 0
			if _check_win(board_copy) == 0:
				return i

    # check if player could win on his next move
    for i in range(0,len(board)):
        board_copy = copy.deepcopy(board)
        if _is_move_valid(board_copy, i):
            board_copy[i] = 1
            if _check_win(board_copy) == 1:
				return i

    # check for space in the corners, and take it
    move = _choose_random_move(board, [0,2,6,8])
    if move != None:
		return move

    # If the middle is free, take it
    if _is_move_valid(board,4):
		return 4


    # else, take one free space on the sides
    move = _choose_random_move(board, [1,3,5,7])
    return move


def is_move_invalid(game_id, index):
    board = games[game_id]
    return board[index] != -1

def _is_move_valid(board, index):
	return board[index] == -1


def main():
    # Create server
    server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, logRequests=True)
    server.register_introspection_functions()
    server.register_function(new_game, 'new_game')
    server.register_function(new_move, 'new_move')
    server.register_function(is_move_invalid, 'is_move_invalid')
    server.register_function(check_win, 'check_win')
    server.register_function(end_game, 'end_game')

    try:
        print "Server is running... You can start playing tic-tac-toe! (Use Control-C to exit)"
        server.serve_forever()
    except KeyboardInterrupt:
        print '...Exiting...'
        quit()

if __name__ == "__main__":
	main()
