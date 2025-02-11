'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''
import random
import math

#returns a random board nXn
def create(n):
    s=list(range(n*n))      # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m="<>v^"                # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n*n*n):  # makes n^3 random moves
        if_legal(s,m[random.randrange(4)])
    return [s,""]           # at the beginning "" is an empty path, later on path
                            # contains the path that leads from the initial state to the state

def get_next(x):            # returns a list of the children states of x
    ns=[]                   # the next state list
    for i in "<>v^":
        s=x[0][:]           # [:] - copies the board in x[0]
        if_legal(s,i)       # try to move in direction i
        # checks if the move was legal and...
        if s.index(0)!=x[0].index(0) and \
           (x[1]=="" or x[1][-1]!="><^v"["<>v^".index(i)]): # check if it's the first move or it's a reverse move
            ns.append([s,x[1]+i])   # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])

def is_target(x):
    n=len(x[0])                     # the size of the board
    return x[0]==list(range(n))     # list(range(n)) is the target state

#############################
def if_legal(x,m):                  # gets a board and a move and makes the move if it's legal
    n=int(math.sqrt(len(x)))        # the size of the board is nXn
    z=x.index(0)                    # z is the place of the empty tile (0)
    if z%n>0 and m=="<":            # checks if the empty tile is not in the first col and the move is to the left
        x[z]=x[z-1]                 # swap x[z] and x[z-1]...
        x[z-1]=0                    # ...and move the empty tile to the left
    elif z%n<n-1 and m==">":        # check if the empty tile is not in the n's col and the move is to the right
        x[z]=x[z+1]
        x[z+1]=0
    elif z>=n and m=="^":           # check if the empty tile is not in the first row and the move is up
        x[z]=x[z-n]
        x[z-n]=0
    elif z<n*n-n and m=="v":        # check if the empty tile is not in the n's row and the move is down
        x[z]=x[z+n]
        x[z+n]=0


def hdistance(s): #This is uniform cost and not based on any heuristic
    return 0

def hdistance1(s): #This will be the simple heuristic of the number of bricks not in place
    counter = 0
    for i in range(len(s[0])):
        if s[0][i] != i  :
            counter+=1
    return counter

def hdistance2(s): #This will be the Manhattan distance heuristic
    return manhattan_distance(s[0])

def manhattan_distance(board):
    size = int(len(board) ** 0.5)
    #find position of where each number should be on 2d board
    target_positions = {}
    for tile in board:
        x = tile//size
        y = tile%size
        target_positions[tile] = (x,y)

    total_distance = 0

    #calculate manhattan distance for each tile
    for i, tile in enumerate(board):
        if tile != 0:  # Skip the empty tile (0)
            row, col = i // size, i % size
            correct_row, correct_col = target_positions[tile]
            #|x1 - x2| + |y1-y2|
            distance = abs(row - correct_row) + abs(col - correct_col)
            total_distance += distance
    return total_distance