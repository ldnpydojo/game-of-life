#!/usr/bin/python

import sys, itertools, random, time

SIZE = (79, 20)
DEAD = '.'
LIVE = '#'

MACROS = [
    """\
.#.
..#
###""", """
.#.
.#.
.#.""", """
##..
##..
..##
..##"""
]


class Board(object):
    def __init__(self):
        self.board = [DEAD*SIZE[0] for _ in range(SIZE[1])]
        for i in range(0):
            self.put(random.randrange(len(self.board[0])),
              random.randrange(len(self.board)), True)

        for i in range(20):
            self.place_macro (
                random.choice (MACROS),
                random.randrange (len (self.board[0])),
                random.randrange (len (self.board))
            )

    def place_macro(self, macro, x, y):
        lines = macro.splitlines ()

        for n_line, line in enumerate (lines):
            for n_thing, thing in enumerate (line):
                self.put (x + n_thing, y + n_line, thing == LIVE)

    def next(self):
        newboard = []
        for y in range(0, len(self.board), 1):
            line = ""
            for x in range(0, len(self.board[0]), 1):
                neighbours = self.neighbours(x, y)
                if self.get(x, y): # alive
                    if 2 <= neighbours <= 3:
                        line += LIVE
                    else:
                        line += DEAD
                else: # dead
                    if neighbours == 3:
                        line += LIVE
                    else:
                        line += DEAD
            newboard.append(line)
        self.board = newboard
        return self

    def get(self, x, y):
        x = x % len(self.board[0])
        y = y % len(self.board)
        return self.board[y][x] == LIVE

    def put(self, x, y, alive):
        x = x % len(self.board[0])
        y = y % len(self.board)
        self.board[y] = self.board[y][:x] + (LIVE if alive else DEAD) + \
            self.board[y][x + 1:]

    def neighbours(self, x, y):
        count = 0
        for x1 in range(x - 1, x + 2, 1):
            for y1 in range(y - 1, y + 2, 1):
                if x1 != x or y1 != y:
                    if self.get(x1, y1):
                        count += 1
        return count

    def __iter__(self):
        return self

    def __repr__(self):
        return '\n'.join(line for line in self.board)

if len(sys.argv) > 1:
    random.seed(sys.argv[1])

b = Board()
while True:
    print "\n" * 20
    print b
    b.next()
    time.sleep(0.3)
