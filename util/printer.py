import sys
sys.path.append('../')

from model import find_chess_piece

def printboard(chess_pieces) :
	for i in range (0, 8) :
		for j in range (0,8) :
			if find_chess_piece(chess_pieces, i, j) == None :
				print('.', end= ' ')
			else :
				chess_piece = find_chess_piece(chess_pieces, i, j)
				print(chess_piece, end=' ')
		print()

def printattack(chess_pieces) :
	countenemy = 0
	countally = 0
	for each in chess_pieces :
		countenemy += each.count_attacked_enemy(chess_pieces)
		countally += each.count_attacked_ally(chess_pieces)
	print(countally, ' ', countenemy)