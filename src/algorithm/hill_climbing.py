import copy
from nything import generate_move
from util.printer import print_board, print_attacked_pieces

def hill_climbing(chess_pieces, max_iteration):
    #inisiasi kondisi
    i = 0
    while (i < max_iteration):
        generate_move(chess_pieces)
        i = i +1

    return chess_pieces