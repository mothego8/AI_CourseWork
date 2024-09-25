
import random #hint -- you will need this for the following code: column=random.randrange(0,size)
import copy
import time

class Propagation:

    def __init__(self, size):
        self.size = size
        self.columns = []
        self.stack = []
        self.constraint = {}
        
    def change_size(self, size):
        self.size = size
        # for i in range(size):
        #     self.constraint[i] = list(range(size))


    def display(self):
        for column in range(self.size):
            for row in range(len(self.columns)):
                if column == self.columns[row]:
                    print(' ♛ ', end=' ')
                else:
                    print(' . ', end=' ')
            print()
    
    def remove_possible_values(self, column, row):
        # Remove the specified row from the list of possible rows for the given column
        # column_row_map[column].remove(row)

        # Remove rows that are diagonally threatened
        for col, rows in self.constraint.items():
            if col != column:
                diagonal_distance = abs(column - col)
                if row - diagonal_distance in rows:
                    rows.remove(row - diagonal_distance)
                if row + diagonal_distance in rows:
                    rows.remove(row + diagonal_distance)
        
        # Remove rows that are horizontally threatened
        for col, rows in self.constraint.items():
            if col != column and row in rows:
                rows.remove(row)

    def solve_queens(self):

        iterations = 1
        moves = 0
        self.columns.clear()
        for i in range(self.size):
            self.constraint[i] = list(range(self.size))
        row = 0
        column = 0
        self.stack.append(copy.deepcopy(self.constraint))
        tic = time.time()
        while True:
            while column < self.size:
                if not self.constraint[column]:
                    iterations += 1
                    old = self.columns.pop()
                    moves += 1
                    if old == -1:
                        print("no solutions")
                        return [0, 0, 0]

                    column -= 1
                    self.constraint = self.stack.pop()
                else:
                    row = random.randrange(0, len(self.constraint[column]))
                    new_row = self.constraint[column][row]
                    self.constraint[column].remove(new_row)
                    self.columns.append(new_row)
                    moves += 1
                    self.stack.append(copy.deepcopy(self.constraint))
                    self.remove_possible_values( column, new_row)
                    column += 1
            if column == self.size:
                toc = time.time()
                # self.display()
                return [iterations, moves, round(1000*(toc-tic), 2)]
