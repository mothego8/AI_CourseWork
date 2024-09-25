import alphaBetaPrunning
import copy
import game
import socket

# Server is ○

HOST = ''
PORT = 8081

def handle_client(conn):
    with conn:
        print(f'Connected by {conn.getpeername()}\n')
        board = game.create()
        game.setMyColor('○','●')
        game.printState(board)
        while not game.isFinished(board):
            data = conn.recv(10)
            if not data:
                conn.close()
                break
            try:
                move = int(data.decode())
                print(f'Received {move}\n')
                if game.isLegal(move, board):
                    game.makeMove(move, board)
                    game.printState(board)
                    # Choose my move
                    my_move = 0
                    next_state = alphaBetaPrunning.go(board)
                    for move in game.legalMoves(board):
                        tmp=copy.deepcopy(board)
                        game.makeMove(move,tmp)
                        if tmp == next_state:
                            my_move = move
                            break
                    board = next_state
                    if my_move == 0:
                        conn.close()
                        break
                    print(f'Played {my_move}\n')
                    game.printState(board)
                    conn.sendall(str(my_move).encode())
                else:
                    conn.sendall(b'Invalid move')
                    conn.close()
                    break
            except ValueError:
                conn.sendall(b'Invalid input')
                conn.close()
                break
        print(board)
        game.printState(board)
        my_score, opp_score, result = game.whoWin(board)
        print(f"Your score is: {my_score}\nOpponent's score is: {opp_score}\nThe result is: {result}\n")
        if result == game.VIC:
            print("You won!")
        elif result == game.LOSS:
            print("You lost!")
        else:
            print("It's a tie!")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on', (HOST, PORT))
    conn, addr = s.accept()
    handle_client(conn)