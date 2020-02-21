# Sudoku
from random import *
from math import *
import numpy as np
import sys
from numpy.core._multiarray_umath import ndarray

def findPreSpot(n, board):
    n = n - 1
    if (board[n // 9][n % 9] != 0):
        n = findPreSpot(n, board)
    return n

def whichSquare(i, j, board):
    sqrCentre_x = [1, 1, 1, 4, 4, 4, 7, 7, 7]
    sqrCentre_y = [1, 4, 7, 1, 4, 7, 1, 4, 7]
    board = np.array(board)
    for ind in range(9):
        if (abs(i - sqrCentre_x[ind]) <= 1 and abs(j - sqrCentre_y[ind] <= 1)):
            if sqrCentre_y[ind] != 7 or sqrCentre_y[ind] != 7:
                square = board[sqrCentre_x[ind] - 1:sqrCentre_x[ind] + 2, sqrCentre_y[ind] - 1:sqrCentre_y[ind] + 2]
                return square
            if sqrCentre_y[ind] != 7 and sqrCentre_x[ind] == 7:
                square = board[6:, sqrCentre_y[ind] - 1:sqrCentre_y[ind] + 2]
                return square
            if sqrCentre_y[ind] == 7 and sqrCentre_x[ind] != 7:
                square = board[sqrCentre_x[ind] - 1:sqrCentre_x[ind] + 2, 6:]
                return square
            if sqrCentre_y[ind] == 7 and sqrCentre_x[ind] == 7:
                square = board[6:, 6:]
                return square

def isInASquare(i, j, num, answer):
    if num in whichSquare(i, j, answer):
        return True
    return False

def isLegal(i, j, answer, num) -> object:
    if (num not in answer[i]) & (num not in [row[j] for row in answer]) and not isInASquare(i, j, num, answer):
        return True
    return False

def sudokuSolver(n, board, answer):
    if n == 80:
        return True
    if (board[n // 9][n % 9] != 0):
        n = n + 1
        return sudokuSolver(n, board, answer)
    if (board[n // 9][n % 9] == 0):
        for num in range(1, 10):
            if isLegal(n // 9, n % 9, answer, num):
                answer[n // 9][n % 9] = num
                n = n + 1
                if sudokuSolver(n, board, answer):
                    return True
                n = findPreSpot(n, board)
                answer[n // 9][n % 9] = 0
    return False

board = (
    (5, 3, 0, 0, 7, 0, 0, 0, 0),
    (6, 0, 0, 1, 9, 5, 0, 0, 0),
    (0, 9, 8, 0, 0, 0, 0, 6, 0),
    (8, 0, 0, 0, 6, 0, 0, 0, 3),
    (4, 0, 0, 8, 0, 3, 0, 0, 1),
    (7, 0, 0, 0, 2, 0, 0, 0, 6),
    (0, 6, 0, 0, 0, 0, 2, 8, 0),
    (0, 0, 0, 4, 1, 9, 0, 0, 5),
    (0, 0, 0, 0, 8, 0, 0, 7, 9)
)
answer = np.array(board)
if sudokuSolver(0, board, answer):
    for i in range(9):
        print(answer[i])
else:
	print("No Solutions for this Sudoku!")