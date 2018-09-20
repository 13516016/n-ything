import sys
sys.path.append('../')

from model import *

def printboard(chess_pieces) :
	for i in range (0, 8) :
		for j in range (0,8) :
			if find_chess_piece(chess_pieces, i, j) == None :
				print('.')
			else :
				chess_piece = find_chess_piece(chess_pieces, i, j)
				print(chess_piece, end=' ')
		print()

def printattack(chess_pieces) :
	countenemy = 0
	countally = 0
	for each in chess_pieces :
		countenemy += each.count_attacked_enemy
		countally += each.count_attacked_ally
	print(countally, ' ', countenemy)