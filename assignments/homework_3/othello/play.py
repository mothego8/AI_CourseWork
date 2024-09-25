import alphaBetaPrunning
import game
import naive
oneMoreChance = False
board=game.create()
game.whoIsFirst(board)
while not game.isFinished(board) or oneMoreChance:
    if game.isHumTurn(board):
        # move = naive.naive_othello_ai(board)
        game.inputMove(board)
        # game.makeMove(move, board)
    else:
        board=alphaBetaPrunning.go(board)
    game.printState(board)
    if (game.isFinished(board) and not(oneMoreChance)):
        if (game.anyLegalMove(board)):
            print ("No more moves - One more chance")
            game.changePlayer(board)
        else:
            oneMoreChance = False
    else:
        oneMoreChance=False
game.printState(board)

