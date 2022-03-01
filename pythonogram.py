#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 23:22:34 2017

Name: Tyeece Hensley
Due Date: September 28,2017
Program: Homework 1
"""

import layout
import random
import time 
import datetime
master=[]
scratch=[]
scratch = [[layout.marker.empty for x in range(layout.columns)] for y in range(layout.rows)]#fills list scratch with empty markers from the layout function
row_tomo=[]
column_tomo=[]
guess_count=0
cor_count=0


#fills master list with randomly positioned emty and full markers from the layout function
for x in range(layout.rows):
    sublist=[]
    for y in range(layout.columns):
        holder=random.randint(0,1)
        if (holder == 0):
            sublist.append(str(layout.marker.empty))
        else:
            sublist.append(str(layout.marker.full))
    master.append(sublist)


#checks every row for a full marker and counts it 
for a in range(layout.rows):
    tomo=[]
    num=0
    for b in range(layout.columns):
        if (master[a][b]=='*'):
            num=num+1
        else:
            if (num==0):
                continue
            else:
                tomo.append(num)
                num=0
    if (num!=0):        
        tomo.append(num)
    row_tomo.append(tomo)


#checks every column for a full markr and counts it
for e in range(layout.columns): 
    todo=[]
    num=0
    for f in range(layout.rows):
        if (master[f][e]=='*'):
            num=num+1
        else:
            if(num==0):
                continue
            else:
                todo.append(num)
                num=0
    if (num!=0):        
        todo.append(num)
    column_tomo.append(todo)

maximum=len(max(column_tomo,key=len))#checks for maximum length element in column list

#fills empty spaces in column list with empty marker for ease of printing 
for g in range(layout.columns):
    while (len(column_tomo[g]))<maximum:
        column_tomo[g].append(layout.marker.empty)        

 
t1=datetime.datetime.now()#takes time at the beginning of the game

while (master != scratch):
    print('\n')
#prints pythonogram and accomodating row and column counts
    for c in range(layout.rows):
        print((layout.board.corner+layout.board.top)*(layout.columns)+layout.board.corner)
        for d in range(layout.columns):
            print(layout.board.side+scratch[c][d],end="")
        print(layout.board.side,(*row_tomo[c]))
    print((layout.board.corner+layout.board.top)*(layout.columns)+layout.board.corner)
    for h in range(maximum):
        for i in range (layout.rows):
            if (column_tomo[i][h]==layout.marker.empty):
                continue
            print('',column_tomo[i][h], end="")
        print('\n')
#asks for users guess and checks if it is correct and increments a count for the statistics    
    guess=(input('Please enter your guess (row,col): '))
    guess_count=guess_count+1
    guess=guess.split(',')
    row=(int(guess[0]))-1
    col=(int(guess[1]))-1
#validates the input to ensure the number entered is within range 
    if (row>=layout.rows or col>=layout.columns):
        print ("Value is too high...Cannot exceed maximum number of rows and columns")
        time.sleep(2)
        continue
    elif (row<0 or col<0):
        print ("Value is too low...The first row and column are considered #1")
        time.sleep(2)
        continue
    if (master[row][col]=='*'):
        scratch[row][col]='*'
        cor_count=cor_count+1
        print('\nCorrect')
        time.sleep(1)
    else:
        print('\nWrong guess....Try Again')
        time.sleep(1)
#prints the board to show the final pattern
for c in range(layout.rows):
    print((layout.board.corner+layout.board.top)*(layout.columns)+layout.board.corner)
    for d in range(layout.columns):
        print(layout.board.side+scratch[c][d],end="")
    print(layout.board.side,(*row_tomo[c]))
print((layout.board.corner+layout.board.top)*(layout.columns)+layout.board.corner)
for h in range(maximum):
    for i in range (layout.rows):
        if (column_tomo[i][h]==layout.marker.empty):
            continue
        print('',column_tomo[i][h], end="")
    print('\n')
print('\nGame Over' )

t2=datetime.datetime.now()#checks time at the end of the game

print("Your accuracy for this game is:",((cor_count/guess_count)*100),'%')
print("The total time taken to comlete this game was:",(t2-t1))
