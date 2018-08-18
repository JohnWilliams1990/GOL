#!/usr/local/bin/python2.7
#  John Williams
#  105201054
#  Date: Sat. Aug. 11, 2018
#  Program: game_of_life.py

from __future__ import print_function
import random
import time 


size = input("Please select a board Size:")
iterations = input("please enter the number of iterations")

def gen_board(size):
	board = []
	for i in range(0,size+2):
		board.append([])
		for j in range(0,size+2):
			if random.randint(0,2) ==1:
				board[i].append(1)
			else: 
				board[i].append(0)
	return board

def print_board(board):
	for i in range(1, size+1):
		for j in range(1, size +2):
			if board[i][j] == 1:
				
				print ("o", end = ' ')
			else:
				print ("-", end = ' ')
		print("")
	print("")
#
#def print_board_count(board):
#	for i in range(1, size+1):
#		for j in range(1, size +2):
#			print (board[i][j], end = ' ')
#		print("")
#	print("")


#[i-1,j-1][i-1,j  ][i-1,j+1]
#[i,  j-1][i  ,j  ][i  ,j+1]
#[i+1,j-1][i+1,j  ][i+1,j+1]
def move(board):
	size = len(board[0]) - 2
	alive = gen_board(len(board))
	for i in range(1, size + 1):
		for j in range(1, size + 1):
			alive[i][j] = board[i-1][j-1] + board [i-1][j] + board[i-1][j+1] + board[i][j-1] + board[i][j+1] + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1]

	#print_board_count(alive):

	for i in range(1, size + 1):
		for j in range(1, size + 1):
			if  board[i][j] == 1:

				if alive[i][j] < 2: 
					 board[i][j] = 0
				elif alive[i][j] > 3: 
					 board[i][j] = 0
			else:
				if  alive[i][j]  == 3:
					board[i][j] = 1
			alive[i][j] = 0
	return board		
 





#move(board,size)

board = gen_board(size)




print(len(board[0]))
for i in range(0,100):
	print_board(board)
	board = move(board) 
	time.sleep(1)

