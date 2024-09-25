import game
import random




def naive_othello_ai(board):
    valid_moves = game.legalMoves(board)
    if valid_moves:
        # Sort valid moves by their evaluation values.
        # valid_moves.sort(key=lambda move: evaluate_move(move), reverse=True)
        return random.choice(valid_moves)  # Choose the move with the highest evaluation.
    return None




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




