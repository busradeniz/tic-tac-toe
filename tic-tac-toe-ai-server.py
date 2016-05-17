from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
	    rpc_paths = ('/tic-tac-toe',)


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
