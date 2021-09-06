# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 22:55:20 2021

@author: Ahat
"""
import matplotlib.pyplot as plt
import random

player = [0,1,2,3]
money = [50,50,50,50]
position = [0,0,0,0]
rentpr= [1,1,1,1]


def rolldice():    
  die1 = random.randint(1,6)    
  die2 = random.randint(1,6)    
  total=die1+die2    #print(die1, die2, roll)    
  return (total)

run = True

def move(pl):
  global run
  roll = rolldice()
  position[pl] += roll
  if position[pl]>39:
      position[pl]-=40
  if board[position[pl]]==' ' and money[pl]>2: #If the property is unowned and the player has enough money to buy the property
      board[position[pl]] = player[pl]
      money[pl]-=3
  else:
      for a in range(0,4):
          if board[position[pl]] == a and (money[1]>=0 and money[0]>=0 and money[2]>=0 and money[3]>=0):
              if pl == a:
                  rentpr[pl]+=1 #If the property is owned by the player, then the rent increases by $1. 
              
              money[pl]-= rentpr[a] 
              money[a]+= rentpr[a]   #If the property is owned, then the player has to pay the owner the rent.
              if money[pl]<0: # if cannot pay the rent, game concludes
                  print('Properties:',board)
                  print('rent:',rentpr)
                  print("Money: ",money)
                  print(f"Player {pl+1} lose.")
                  run = False
                  
        

board = []
for i in range(0,40):
  board.append(' ')

'''Game code'''
while run:
    for i in player:
        move(i)

'''Winner determination'''
maxim = 0 
for char in money:
    if char>maxim:
        maxim = char
        
if money[0]> money[1] and money[0]> money[2] and money[0]>money[3]:
    print("Player 1 win.")
elif money[1]> money[0] and money[1]> money[2] and money[1]>money[3]:
    print("Player 2 win.")
elif money[2]> money[1] and money[2]> money[0] and money[2]>money[3]:
    print("Player 3 win.")
elif money[3]> money[1] and money[3]> money[2] and money[3]>money[0]:
    print("Player 4 win.")



'''Graph of each player’s bank account '''
players = ['1','2','3','4']
plt.figure(figsize = (10,6))
plt.title('Graph of bank accounts of players 1-4', fontsize=20)
plt.bar(players, money, color = 'purple', linewidth = 1, width = 0.30)
plt.xlabel("Players", fontsize=15)
plt.ylabel("Money",fontsize=15)
plt.show()

           
'''Play Eastonoply 3 times and report the number of moves player 1 made during each game.'''
positions = [0,0,0,0]

def move1(ply):
    roll = rolldice()
    positions[ply] += roll
    if positions[ply]>39:
        positions[ply]-=40
    if board[positions[ply]]==' ' and money[ply]>2:
        board[positions[ply]] = player[ply]
        money[ply]-=3
    else:
        for a in range(0,4):
            if board[positions[ply]] == a and (money[1]>=0 and money[0]>=0 and money[2]>=0 and money[3]>=0):
                if ply == a:
                    rentpr[ply]+=1
                money[ply]-= rentpr[a]
                money[a]+= rentpr[a]
    if ply == 0:
        print('Player', (ply+1), 'Position',positions[ply]) #reporting the number of moves and positions of player 1 in three times
    
for b in range(1,4):     # playing it for 3 times   
    for j in player:
        move1(j)

