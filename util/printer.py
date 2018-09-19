import sys
sys.path.append('../')

from model import *

def printer(chess_pieces) :
	for i in range (0, 8) :
		for j in range (0,8) :
			if find_chess_piece(chess_pieces, i, j) == None :
				print('.')
			else :
				chess_piece = find_chess_piece(chess_pieces, i, j)
				print(chess_piece, end=' ')
		print()