# Sudoku Solver
from random import *
from math import *
import numpy as np
import sys
from numpy.core._multiarray_umath import ndarray
import pygame
from tkinter import messagebox


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def printText(text, row, column, color):
    font = pygame.font.Font('freesansbold.ttf', 36)
    TextSurf, textRect = text_objects(text,font, color)
    textRect.center = ((MARGIN + HEIGHT) * row + MARGIN + (HEIGHT // 2),(MARGIN + WIDTH) * column + MARGIN +(WIDTH // 2))
    screen.blit(TextSurf, textRect)

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
answer = list(answer)
print(type(answer))
#-----------------------------------------------
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 60
HEIGHT = 60
 
# This sets the margin between each cell
MARGIN = 10
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(9):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(9):
        grid[row].append(board[row][column])  # Append a cell
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [640, 640]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Sudoku!")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            print("Click ", pos, "Grid coordinates: ", row, column)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                grid[row][column] = 1
            if event.key == pygame.K_2:
                grid[row][column] = 2
            if event.key == pygame.K_3:
                grid[row][column] = 3
            if event.key == pygame.K_4:
                grid[row][column] = 4
            if event.key == pygame.K_5:
                grid[row][column] = 5
            if event.key == pygame.K_6:
                grid[row][column] = 6
            if event.key == pygame.K_7:
                grid[row][column] = 7
            if event.key == pygame.K_8:
                grid[row][column] = 8
            if event.key == pygame.K_9:
                grid[row][column] = 9
            if event.key == pygame.K_SPACE:
                grid[row][column] = 0

    # If you won the game

    # Set the screen background
    screen.fill(WHITE)
    
    # Draw the grid
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                color = (128,128,128)
            else:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * c + MARGIN,
                              (MARGIN + HEIGHT) * r + MARGIN,
                              WIDTH,
                              HEIGHT])

    for r in range(9):
        for c in range(9):
            if (grid[c][r] > 0) and (grid[c][r]==answer[c][r]):
                printText(str(grid[c][r]), r, c, GREEN)
            elif (grid[c][r] > 0):
                printText(str(grid[c][r]), r, c, RED)
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()