import time
import random

class Min_Conflict:

    def __init__(self, size):
        self.size = size
        self.columns = []
        self.conflicts = [] 

    def change_size(self, size):
        self.size = size

    def place_n_queens(self):
        self.columns.clear()
        row = 0
        while row < self.size:
            column=random.randrange(0,self.size)
            self.columns.append(column)
            row+=1
        self.num_of_conflicts()

    def display(self):
        for column in range(self.size):
            for row in range(self.size):
                if column == self.columns[row]:
                    print(' ♛ ', end=' ')
                else:
                    print(' . ', end=' ')
            print()


    def num_of_conflicts(self):
        n = self.size
        self.conflicts = [0] * n  # Initialize a list to store the attack count for each spot

        for i in range(n):
            for j in range(n):
                if i != j:  # Skip checking a spot against itself
                    # Check if the spot attacks the same row
                    if self.columns[i] == self.columns[j]:
                        self.conflicts[i] += 1
                    # Check if the spot attacks diagonally
                    if abs(self.columns[i] - self.columns[j]) == abs(i - j):
                        self.conflicts[i] += 1


    def row_conf(self, col):
        n = self.size
        row_conflicts = [0] * self.size

        # loops through all potential rows 
        for j in range(n):
            # Check conflicts in the same column (vertical)
            for i in range(n):
                # every queen that isnt itself that has the same row 
                if i != col and self.columns[i] == j:
                    row_conflicts[j] += 1

            # Check conflicts in diagonals
            for i in range(n):
                # every queen that isn't itself that is on the same diagonal
                if i != col:
                    diff_col = abs(col - i)
                    diff_row = abs(j - self.columns[i])
                    if diff_col == diff_row:
                        row_conflicts[j] += 1

        return row_conflicts

    def update_conflicts(self, col, new_row, min_conf):
        # set the amount of conflicts of moving to that row to our queen 
        self.conflicts[col] = min_conf  

        # get our old row so we can update conflicts
        old_row = self.columns[col]
        
        for col2, row2 in enumerate(self.columns):
            if col == col2:
                continue
            # now we need to change the amount of conflicts our queen caused from being in its old row
            if (old_row == row2) or (abs(old_row - row2) == abs(col - col2)):
                self.conflicts[col2] -= 1
            # and add all to the other rows the conflicts our queen is now causing them
            if (new_row == row2) or (abs(new_row - row2) == abs(col - col2)):
                self.conflicts[col2] += 1
              


    def solve_queens(self):
        self.place_n_queens()
        # initialize number of conflicts for each queen
        # self.num_of_conflicts() # O(n)
        iterations = 1
        moves = 8
        tic = time.time()
        while sum(self.conflicts) != 0:
            iterations += 1
            # pick a queen that has at least one conflict
            valid_queens = [i for i, value in enumerate(self.conflicts) if value > 0]
            queen = random.choice(valid_queens) 

            # a map of all the rows and what the conflicts would be if we switchewd our queen to that row 
            row_confs = self.row_conf(queen)

            # gets the row with the fewest conflict
            min_conf = min(row_confs) 

            # gets the index of row with fewest conlfict. 
            # since many rows could have the same fewest conflicts we choose this index randomly from the set of
            # rows with this fewest conflicts
            valid_rows = [i for i, value in enumerate(row_confs) if value == min_conf]
            new_row = random.choice(valid_rows) 
            
            # update conflicts
            # we update how many conflicts the queen will now have at its new row
            # and we remove the conflicts the queen being in the prev row was causing
            self.update_conflicts(queen, new_row, min_conf)
        
            # we officially change the row of our queen
            self.columns[queen] = new_row
            moves+=1
            temp = time.time()
            if(temp - tic > 0.1):
                self.place_n_queens()
                moves += 8
        toc = time.time()
        # self.display()
        return [iterations, moves, round(1000*(toc-tic), 2)]
