import sys
sys.path.append('../')

from model import *

def fitness(chess_pieces) :
	countenemy = 0
	countally = 0
	for each in chess_pieces :
		countenemy += each.count_attacked_enemy(chess_pieces)
		countally += each.count_attacked_ally(chess_pieces)
	return(countally, countenemy)