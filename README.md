# Pythonogram: Picross in Python
## Introduction
Pythonogram is an interactive nonogram puzzle solver. It is essentially just like Picross
developed for the Nintendo DS, except written in Python. Pythonogram consists of two
grids: a master grid in which certain cells are filled and others are blank, and an empty
grid in which all cells are blank. Players are presented with the empty grid and required
to makes guesses. These guesses correspond to cell locations and are “good” guesses if the
corresponding location is filled in the master; guesses are “bad” otherwise. The objective of
the game is to find all of the filled cells in the master. Overall score is based on how many
guesses were required to do so, and the amount of time it took.
So that players do not have to guess randomly, they are presented with clues. Specifically,
for each row and column, there is a list of numbers corresponding to the number of filled
cells in that row or column, along with their distribution. This effectively makes the game
a logic puzzle known as a nonogram. From Wikipedia:
>...the numbers are a form of discrete tomography that measures how many
unbroken lines of filled-in squares there are in any given row or column. For
example, a clue of “4 8 3” would mean there are sets of four, eight, and three
filled squares, in that order, with at least one blank square between successive
groups.

It is your job to not only create such a puzzle, but to develop the interaction in which users
can make guesses against that puzzle.
