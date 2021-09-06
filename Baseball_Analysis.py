# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:11:20 2021

@author: ahato
"""

import csv

class Atbat(object):
  def __init__(self,inning,top,ab_id,g_id,p_score,batter_id,pitcher_id,stand,p_throws,event,o):
                self.inning = inning
                self.top = top
                self.ab_id = ab_id
                self.g_id = g_id
                self.p_score = p_score
                self.batter_id = batter_id
                self.pitcher_id = pitcher_id
                self.stand=stand                
                self.p_throws=p_throws
                self.event = event
                self.o = o

class Player(object):
  def __init__(self,player_id,first_name,last_name,event):
                self.player_id = player_id
                self.first_name = first_name
                self.last_name = last_name
                self.event = event
                           
def idfind(players, player_id):
    for j in range(len(players)):
        if players[j].player_id == player_id:
            return(j)
    return (-1)


atbat = []

for i in range(0,30):
    file='10000AtBats.csv'
    with open (file) as csvfile:
        readcsv=csv.reader(csvfile,delimiter=',')
        cnt=0
        for row in readcsv:
            if cnt>=1:
                #print (row)
                batter_id=[row[5]]
                pitcher_id=[row[6]]
                inning=[row[0]]
                top=[row[1]]
                ab_id=[row[2]]
                g_id=[row[3]]
                p_score=[row[4]]
                stand=[row[7]]
                p_throws = [row[8]]
                event = [row[9]]
                o = [row[10]]
                atbat.append(Atbat(inning,top,ab_id,g_id,p_score,batter_id,pitcher_id,stand,p_throws,event,o))
            cnt+=1
    

players = []

pl = 'player_names.csv'
with open (pl, 'r') as csvfile:
    readpl = csv.reader(csvfile, delimiter=',')
    for i in range(len(atbat)):
        batid = atbat[i].batter_id
        compid = idfind(players,batid)
        if compid == -1:
            event = []
            firstnm=''
            lastnm=''
            players.append(Player(batid,firstnm,lastnm,event))
        else:
            players[compid].event.append(atbat[i].event)
print(players[2].event)
