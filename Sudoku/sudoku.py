# Author: Muneeb Azam - CS486: Introduction to Artificial Intelligence
#
# import statements
from collections import namedtuple
from sets import Set
import numpy
import time
import sys

# An entry refers to a cell in the sudoku board
# which has an x and y coordinate 
Entry = namedtuple('Entry', 'x y')


# funcion which checks if the passed value 
# exists already in that square of the board
def check_square(board, entry, value):
    # finds the starting row and col of that square
    start_col = entry.y - (entry.y % 3)
    start_row = entry.x - (entry.x % 3)
    
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == value:
                return False
            
    return True


# function which checks if the passed value
# exists already in that row of the board
def check_row(board, entry, value):
    for i in range(9):
        if board[entry.x][i] == value:
            return False
    return True


# function which checks if the passed value
# exists already in that column of the board
def check_column(board, entry, value):
    for i in range(9):
        if board[i][entry.y] == value:
            return False
    return True
    

# function which checks the constraints given the
# most recent value assignment
def check_constraints(board, entry, value):
    return check_square(board, entry, value) and \
           check_row(board, entry, value) and \
           check_column(board, entry, value)


# function which finds the next entry on the
# board which has yet to be asigned (has a val of 0)
def next_entry(board):
    next_var = None
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                next_var = Entry(i, j)
                break
    return next_var


# function called once to initialize the game 
# board from the provided .sd sudoku file 
def generate_grid(sd_file):
    board = []
    with open(sd_file) as file:
        for row in file:
            line = row.split()
            line = [int(i) for i in line]
            if len(line) > 0:
                board.append(numpy.array(line))
    return numpy.array(board)


# function called once to initialize the domain
# grid which keeps track of the domain for each
# cell used in version B and C (forward checking)
def generate_domain_grid(board):
    domain = Set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    domainBoard = []
    for i in range(1, 10):
        x = []
        for j in range(1, 10):
            # if the cell is zero then the domain
            # could possibly be any number from 1 to 9
            if (board[i-1][j-1] == 0):
                x.append(domain)
            # if the cell is already filled in the 
            # domain for the cell is that fixed
            else:
                x.append(Set([10]))
        domainBoard.append(x)
    return domainBoard

# main algorithm to solve the sudoku board using backtracking search
def solve_sudoku(num_values, num_instance):

    # construct the file path sudoku_problems/<num_values>/<num_instance>.sd
    file_path = 'sudoku_problems/' + str(num_values) + '/' + str(num_instance) + '.sd'

    # generate game board
    board = generate_grid(file_path)

    # generate domain board
    domainBoard = generate_domain_grid(board)

    # start timer
    startTime = time.time()
    
    # run main algorithm
    completed = backtracking_search(board, 0)

    # stop the timer and exit
    print "Completion Time: " + str((time.time() - startTime))
    return completed


# main backtracking search algorithm for version A (no forward checking + heuristics)
def backtracking_search(board, numSteps):
    
    # find next empty cell to assign
    assignment = next_entry(board)
    
    # board is filled, return board and number of assignments
    if assignment == None:
        print "The Solution is: "
        print(board)
        print "Number of Steps: " + str(numSteps)
        return True
    
    # loop through all values in the domain
    for i in range(1, 10):

        # check the constraints given the new i value we are about to assign
        if check_constraints(board, assignment, i):
            
            # since we have passed the constraints we can assign this value
            # and increment the number of assignments by one
            board[assignment.x][assignment.y] = i
            numSteps += 1
            
            # call backtracking algorithm recursively as per class notes
            if backtracking_search(board, numSteps):
                return True
            
            # If assignment didnt work and we backtracked we set the
            # cell in the board back to zero
            board[assignment.x][assignment.y] = 0
            
    return False


# function which checks to see if the domain of any cell
# is empty meaning we can't continue with these assignments
# used for version B with forward checking
def check_failures(domainBoard):
    for i in range(9):
        for j in range(9):
            if (len(domainBoard[i][j]) == 0):
                return False;
    return True;

solve_sudoku(sys.argv[1], sys.argv[2])
