import xmlrpclib

def print_board(board):

    print "The board look like this: \n"

        for i in range(3):
            print " ",
                for j in range(3):
                    if board[i*3+j] == 1:
                        print 'X',
                        elif board[i*3+j] == 0:
                            print 'O',
                        elif board[i*3+j] != -1:
                            print board[i*3+j]-1,
                        else:
                            print ' ',

                        if j != 2:
                            print " | ",
                print

                if i != 2:
                    print "-----------------"
                else:
                    print

def print_instruction():
    print "Please use the following cell numbers to make your move"
        print_board([2,3,4,5,6,7,8,9,10])


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