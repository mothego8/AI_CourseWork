import time
import random

class BM:

    def __init__(self, size):
        self.size = size
        self.columns = []

    def change_size(self, size):
        self.size = size

    def place_n_queens(self, size):
        self.columns.clear()
        row = 0
        while row < size:
            column=random.randrange(0,size)
            self.columns.append(column)
            row+=1

    def display(self):
        for row in range(len(self.columns)):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('♛', end=' ')
                else:
                    print(' .', end=' ')
            print()

    def is_valid_n_queens(self, board):
        n = len(board)  # The size of the board

        # Check for diagonal attacks
        for i in range(n):
            for j in range(i + 1, n):
                if abs(board[i] - board[j]) == abs(i - j):
                    return False

        # Check for horizontal attacks (same row)
        for i in range(n):
            for j in range(i + 1, n):
                if board[i] == board[j]:
                    return False

        # No conflicts found, the placement is valid
        return True

    def solve_queens(self):
        num_m = 0
        num_i = 0
        tic = time.time()
        while True:
            self.place_n_queens(self.size)
            num_m += 8
            num_i += 1
            if(self.is_valid_n_queens(self.columns)):
                toc = time.time()
                # self.display()
                return[num_i, num_m, round((toc-tic), 2)]


