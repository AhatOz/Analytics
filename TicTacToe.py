# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:57:52 2021

@author: ahato
"""

import sys

def move(symbol):
  x = int(reader.readline())
  y = int(reader.readline())
  if board[x][y] == " ":
    board[x][y]=symbol
    if rowwin(symbol, x) == True or colwin(symbol, y) == True:
      print("Winning move at {} {}".format(x,y))
    if m == n and diag(symbol) == True:
      print("Winning move at {} {}".format(x,y))
      
  else:
    print("Invalid move at {} {}".format(x,y))

def rowwin(a,row):
  winrow = True
  for j in range(0,m):
    if board[row][j] != a:
      winrow = False
  return(winrow)

def colwin(b,col):
  wincol = True
  for k in range(0,m):
    if board[k][col] != b:
      wincol = False
  return(wincol)
  
def diag(symb):
  windiag = True
  for i in range(m):
    if board[i][i] != symb:
      windiag = False
  return(windiag)


if len(sys.argv) > 1:
    reader = open(sys.argv[1])
else:
    reader = sys.stdin

m = int(reader.readline())
n = int(reader.readline())

if m > 0 and n > 0 and m <= 256 and n <= 256:
    board = []
    for i in range(m):
        board.append([])
        for j in range(n):
            board[i].append(" ")

for i in range(0,m):
  move("X")
  move("O")
  

  
