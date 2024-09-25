import copy
EMPTY, BLACK, WHITE = '.', '●', '○'
HUMAN, COMPUTER = '●', '○'

UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)
VIC=10000000 #The value of a winning board (for max)
LOSS=-VIC #The value of a losing board (for max)
TIE=0 #The value of a tie

'''
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
   the comp's cells = COMPUTER and the human's = HUMAN
1. The heuristic value of the state.
2. Who's turn is it: HUMAN or COMPUTER
3. flag to end game

'''

def value(s):
#Returns the heuristic value of s
        ### your code here ###

        # mobility - num of movs for each player
        # scaled to 100
        # not sure how much this helps and makes game much slower so commenting out
        # max_moves, min_moves = numMoves(s)
        # if (max_moves + min_moves != 0):
        #     mobility  = 100 * (max_moves - min_moves) / (max_moves + min_moves)
        # else:
        #     mobility = 0

        # utility - utility score for each player 
        # based on positional values of each of its pieces
        max_utility , min_utility = utilityScore(s)
        utility = max_utility - min_utility

        # corners captured - num of corners each player captured
        # scaled to 100
        max_corners, min_corners = numCorners(s)
        if ( max_corners + min_corners != 0):
            corners =	100 * (max_corners - min_corners) / (max_corners + min_corners)
        else:
            corners = 0

        # coin parity - num of coins each player has on board
        # scaled to 100
        max_coins, min_coins = numCoins(s)
        coin_parity = 100 * (max_coins - min_coins) / (max_coins + min_coins)

        # add heursitics together
        s[1]= coin_parity + corners + utility #+ mobility
        return s[1]


def utilityScore(s):
    compScore = 0
    humanScore = 0
    for sq in squares():
        piece = s[0][sq]
        if piece == COMPUTER:
            compScore += evaluate_move(sq)
        elif piece == HUMAN:
            humanScore += evaluate_move(sq)

    return [compScore, humanScore]

def evaluate_move(move):
    # Define the value of each board position (corners and edges are more valuable).
    position_values = [
            [4, -3, 2, 2, 2, 2, -3, 4],
            [-3, -4, -1, -1, -1, -1, -4, -3],
            [2, -1, 1, 0, 0, 1, -1, 2],
            [2, -1, 0, 1, 1, 0, -1, 2],
            [2, -1, 0, 1, 1, 0, -1, 2],
            [2, -1, 1, 0, 0, 1, -1, 2],
            [-3, -4, -1, -1, -1, -1, -4, -3],
            [4, -3, 2, 2, 2, 2, -3, 4]
    ]

    x, y = (move//10) - 1, (move%10) - 1
    value = position_values[x][y]
    return value


def numCoins(s):
    # counts num of coins for each player
    computerScore=0
    humanScore=0
    for sq in squares():
        piece = s[0][sq]
        if piece == COMPUTER:
            computerScore += 1
        elif piece == HUMAN:
            humanScore += 1
    return [computerScore, humanScore]

def numMoves(s):
    # counts num of moves for each player
    humanMoves = 0
    compMoves = 0
    compMoves = len(legalMoves(s))
    changePlayer(s)
    humanMoves = len(legalMoves(s))
    changePlayer(s)
    return [compMoves, humanMoves]

def numCorners(s):
    # counts num of corners each player has captured
    compCorners = 0
    humCorners = 0
    corners = [s[0][11], s[0][18], s[0][81], s[0][88]]
    for i in corners:
        if HUMAN == '●':
            if i == '●':
                humCorners += 1
            elif i == '○':
                compCorners += 1
        else:
            if i == '○':
                humCorners += 1
            elif i == '●':
                compCorners += 1
    return [compCorners, humCorners]

#The user decides who plays first
def whoIsFirst(s):
    global HUMAN,COMPUTER
    s[2]=HUMAN ### your code here ###
    return s


def setMyColor(my_color, opp_color):
    global HUMAN,COMPUTER
    COMPUTER = my_color
    HUMAN = opp_color

def isHumTurn(s):
#Returns True iff it the human's turn to play
    return s[2]==HUMAN

def squares():
    return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]

#The HUMAN plays first (=BLACK)
def create():
    global HUMAN,COMPUTER
    board = [EMPTY] * 100
    for i in squares():
        board[i] = EMPTY
    board[44], board[45] = WHITE, BLACK
    board[54], board[55] = BLACK, WHITE
    HUMAN, COMPUTER = '●', '○'
    return [board,0.00001, HUMAN,False]

def printState(s):
    rep = ''
    rep += '  %s\n' % ' '.join(map(str, range(1, 9)))
    for row in range(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(s[0][begin:end]))
    print(rep)

    if s[1] == VIC:
        print("Ha ha ha I won!")
    elif s[1] == LOSS:
        print("You did it!")
    elif s[1] == TIE:
        print("It's a TIE")

def inputMove(s):
# Reads, enforces legality and executes the user's move.

    flag=True
    while flag:
        printState(s)
        move=int(input("To make your move enter a two digits number, the first number is row and the second is column" "\n" \
        "For example: if you want to choose the first row and the third column enter 13" "\n"\
        "Enter your next move: "))
        if isLegal(move, s) ==False:
            print("Illegal move.")
        else:
            flag=False
            makeMove(move,s)


def isFinished(s):
#Returns True if the game ended
    return not anyLegalMove(s)

def isLegal(move, s):
    hasbracket = lambda direction: findBracket(move, s, direction)
    return s[0][move] == EMPTY and any(map(hasbracket, DIRECTIONS))

# get a list of legal moves for the player
def legalMoves(s):
    return [sq for sq in squares() if isLegal(sq, s)]

# Is there any legal move for this player
def anyLegalMove(s):
    isAny = any(isLegal(sq, s) for sq in squares())
    if (not(isAny)):
        s[3] = True
    return isAny

def makeFlips(move, s, direction):
    bracket = findBracket(move, s, direction)
    if not bracket:
        return
    square = move + direction
    while square != bracket:
        s[0][square] = s[2]
        square += direction

def changePlayer(s):
    if s[2] == COMPUTER:
            s[2] = HUMAN
    else:
       s[2] = COMPUTER

def makeMove(move, s):
    s[0][move] = s[2]
    for d in DIRECTIONS:
        makeFlips(move, s, d)
    value(s)
    changePlayer (s)
    return s

def whoWin(s):
    computerScore=0
    humanScore=0
    for sq in squares():
        piece = s[0][sq]
        if piece == COMPUTER:
            computerScore += 1
        elif piece == HUMAN:
            humanScore += 1
    if (computerScore>humanScore):
        return computerScore, humanScore, VIC
    elif (computerScore<humanScore):
        return computerScore, humanScore, LOSS
    elif (computerScore==humanScore):
        return computerScore, humanScore, TIE


def isValid(move):
    return isinstance(move, int) and move in squares()

def findBracket(square, s, direction):
    bracket = square + direction
    if s[0][bracket] == s[2]:
        return None
    opp = BLACK if s[2] == WHITE else WHITE
    while s[0][bracket] == opp:
        bracket += direction
    return None if s[0][bracket] in (EMPTY) else bracket

def getNext(s):
# returns a list of the next states of s
    ns=[]
    for m in legalMoves(s):
        tmp=copy.deepcopy(s)
        makeMove(m,tmp)
        ns+=[tmp]
    return ns