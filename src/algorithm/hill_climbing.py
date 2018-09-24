import copy
from nything import generate_move
from util.printer import print_board, print_attacked_pieces

def hill_climbing(chess_pieces, generate_move, max_iteration):
    #inisiasi kondisi
    print_board(chess_pieces)
    print_attacked_pieces(chess_pieces)
    i = 0
    while (i < max_iteration):
    	generate_move(chess_pieces)
    	i = i +1
    	print(i)

    print_board(chess_pieces)
    print_attacked_pieces(chess_pieces)

    return 