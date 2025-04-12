# Tic-tac-toe

Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.

## Overview

Tic Tac Toe is one of the classic games most of us have played in our childhood. The game rules are pretty simple. There are 2 players that take turns marking a position on an n \* n board. The first player that makes n marks horizontally, vertically, or diagonally, wins the game.

The brute force approach to solve this problem is to iterate over the entire board of size n \* n and check if the current player has marked any row, column, diagonal or anti-diagonal.

This approach is exhaustive and requires
O
(
n
2
)
O(n
2
) time for every move. Let's look at other more efficient approaches to solve the problem.

Accepted
