import time
import random

class DFS:

    def __init__(self, size):
        self.size = size
        self.columns = []

    def change_size(self, size):
        self.size = size

    def display(self):
        for row in range(len(self.columns)):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('♛', end=' ')
                else:
                    print(' .', end=' ')
            print()

    def place_in_next_row(self, column):
        self.columns.append(column)

    def remove_in_current_row(self):
        if len(self.columns) > 0:
            return self.columns.pop()
        return -1

    def next_row_is_safe(self, column):
        row = len(self.columns)
        # check column
        for queen_column in self.columns:
            if column == queen_column:
                return False

        # check diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False

        # check other diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                == (self.size - column) - row):
                return False
        return True

    def solve_queens(self):
        # size = size
        self.columns.clear()
        number_of_moves = 0 
        number_of_iterations = 0
        row = 0
        column = 0
        tic = time.time()
        # iterate over rows of board
        while True:
            #place queen in next row
            while column < self.size:
                number_of_iterations+=1
                if self.next_row_is_safe(column):
                    self.place_in_next_row(column)
                    number_of_moves += 1
                    row += 1
                    column = 0
                    break
                else:
                    column += 1
            # if I could not find an open column or if board is full
            if (column == self.size or row == self.size):
                number_of_iterations+=1
                # if board is full, we have a solution
                if row == self.size:
                    toc = time.time()
                    # print("I did it! Here is my solution")
                    # self.display()
                    return [number_of_iterations, number_of_moves, round(1000*(toc-tic), 2)]
                # I couldn't find a solution so I now backtrack
                prev_column = self.remove_in_current_row()
                if (prev_column == -1): #I backtracked past column 1
                    print("There are no solutions")
                    return [number_of_iterations, number_of_moves,  0]
                number_of_moves +=1
                # try previous row again
                row -= 1
                # start checking at column = (1 + value of column in previous row)
                column = 1 + prev_column

