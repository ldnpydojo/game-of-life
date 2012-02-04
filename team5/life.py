import os
import random
import time
import sys

from colorama import init, Back
init()

WIDTH = 170
HEIGHT = 42 # Not really



def printer(board):
    """
    Print a board

    Arguments:
    - `board`:
    """
    os.system("clear")
    print '  ' + "-" * (WIDTH + 1)
    for row in board:
        sys.stdout.write("  |")
        for cell in row:
            if cell:
                sys.stdout.write(Back.RED + "*" + Back.RESET)
            else:
                sys.stdout.write(" ")
        sys.stdout.write("|\n")
    print '  ' + "-" * (WIDTH + 1)

def create_board():
    """
    Create a random board
    """
    board = [[False for x in xrange(WIDTH)] for y in xrange(HEIGHT)]
    for row in board:
        for i, cell  in enumerate(row):
            if i % random.randint(1, 10) == 0:
                row[i] = True
    return board


def life():
    """
    The game of life
    """
    printer(create_board())

def neighbours(x, y):
    for dx in range(-1, 2):
        for dy in range (-1, 2):
            if dy == dx == 0:
                continue
            yield x + dx, y + dy

# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def is_alive(x, y, board):
    live_n = 0
    height = len(board)
    width = len(board[0])
    for nx, ny in neighbours(x, y):
        live_n += 1 if board[ny % height][nx % width] else 0
    if live_n < 2:
        return False
    elif live_n == 3:
        return True
    elif 2 <= live_n <= 3:
        return board[y][x]
    else:
        return False



def tick(board):
    new_board = []
    height = len(board)
    width = len(board[0])
    for y in range(height):
        row = []
        for x in range(width):
            row.append(is_alive(x, y, board))
        new_board.append(row)
    return new_board

def main():
    """
    GO
    """
    board = create_board()
    while True:
        printer(board)
        time.sleep(0.1)
        board = tick(board)

if __name__ == '__main__':
    main()
