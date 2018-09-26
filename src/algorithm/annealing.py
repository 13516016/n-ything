from nything import generate_move, generate_move_random, more_optimal, fitness
from util.printer import print_board, print_attacked_pieces
import copy
import math
import random

def get_probability(temperatur, const):
	if (temperatur==0):
		return 0
	return math.exp(const / temperatur)

def pieces_comparing(chess_pieces, random_pieces, temperatur):
	min_same_color_attacks, max_different_color_attacks = fitness(chess_pieces)
	same_color_attacks, different_color_attacks = fitness(random_pieces)

	if (more_optimal(min_same_color_attacks, max_different_color_attacks, random_pieces)):
		result_pieces = copy.deepcopy(random_pieces)
	else:
		probability = get_probability(temperatur , ((different_color_attacks - same_color_attacks) - (max_different_color_attacks - min_same_color_attacks)))
		if (random.random() < probability):
			result_pieces = copy.deepcopy(random_pieces)
		else:
			result_pieces = copy.deepcopy(chess_pieces)

	return result_pieces

def annealing(chess_pieces, max_iteration, initial_temperature, descent_rate, iteration_per_change):
	curr_temp = initial_temperature
	#iterasi untuk perubahan temperatur
	curr_iteration = 0
	#iterasi utuk total yg pernah dilakukan
	curr_all_iteration = 0

	while (curr_all_iteration < max_iteration):
		random_pieces = generate_move_random(chess_pieces)
		chess_pieces = pieces_comparing(chess_pieces, random_pieces, curr_temp)
		if (curr_iteration >= iteration_per_change):
			curr_temp = curr_temp - descent_rate
			curr_iteration = -1

		curr_iteration = curr_iteration + 1
		curr_all_iteration = curr_all_iteration + 1
	return chess_pieces
