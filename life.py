#
# life.py - Game of Life lab
#
# Name:Robert Frusina
# Pledge:I pledge my honor that I have abided by the Stevens Honor System
#

import random 
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width,height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == height - 1 or row == 0 or col == 0 or col == width - 1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(width,height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == height - 1 or row == 0 or col == 0 or col == width - 1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice( [1,0] )
    return A

def copy(A):
    newA = []
    for row in A:
        if type(row) is list:
            newA.append(copy(row))
        else:
            newA.append(row)
    return newA

def innerReverse(A):
    height = (len(A))
    width = len(A[0])
    for row in range(height):
        for col in range(width):
            if row == height - 1 or row == 0 or col == 0 or col == width - 1:
                A[row][col] = 0
            elif A[row][col] == 0:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def countNeighbors(row,col,A):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            count += A[r][c]
    count -= A[row][col]
    return count

def next_life_generation(A):
    newA = copy(A)
    height = (len(newA))
    width = len(newA[0])
    for row in range(height):
        for col in range(width):
            if row == height - 1 or row == 0 or col == 0 or col == width - 1:
                A[row][col] = 0
            elif countNeighbors(row, col, A) < 2:
                A[row][col] = 0
            elif countNeighbors(row, col, A) > 3:
                A[row][col] = 0
            elif countNeighbors(row, col, A) == 3:
                A[row][col] = 1
    return newA