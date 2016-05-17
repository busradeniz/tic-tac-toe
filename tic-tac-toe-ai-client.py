import xmlrpclib
def main():
    tic_tac_toe = xmlrpclib.ServerProxy('http://localhost:8000/tic-tac-toe')
    game_id = tic_tac_toe.new_game()

    print "New game is started! Game Id: " + str(game_id)


if __name__ == "__main__":
    main()