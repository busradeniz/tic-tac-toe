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
