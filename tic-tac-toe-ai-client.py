import xmlrpclib
def main():
    tic_tac_toe = xmlrpclib.ServerProxy('http://localhost:8000/tic-tac-toe')
    game_id = tic_tac_toe.new_game()

    print "New game is started! Game Id: " + str(game_id)

	win = False
	move = 0
	while not win:

		# Get player input
		user = get_input()
		while tic_tac_toe.is_move_invalid(game_id, user):
			print "Invalid move! Cell already taken. Please try again.\n"
			user = get_input()
		board = tic_tac_toe.new_move(game_id, user)
		print_board(board)

		# Continue move and check if end of game
		move += 2
		if move > 4:
			winner = tic_tac_toe.check_win(game_id)
			if winner != -1:
				out = "The winner is "
				out += "X" if winner == 1 else "O"
				out += ""
				tic_tac_toe.end_game(game_id)
				quit_game(board, out)
			elif move >= 9:
				tic_tac_toe.end_game(game_id)
				quit_game(board, "No winner")


if __name__ == "__main__":
    main()