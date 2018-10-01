from nything import *
from util.printer import print_board, print_attacked_pieces
from random import randint
import copy
import time

def genetic(chess_pieces, size, banyakiterasi):
	population = initPopulation(chess_pieces,size)

	sortedpopulation = sorted(population, key=fitness_genetic, reverse=True)

	for i in range(0,banyakiterasi):

		sortedpopulation.extend(reproduce(sortedpopulation[0],sortedpopulation[1]))
		sortedpopulation.extend(reproduce(sortedpopulation[1],sortedpopulation[2]))

		sortedpopulation = sorted(sortedpopulation, key=fitness_genetic, reverse=True)

	return sortedpopulation[0]

def fitness_genetic(individual):

	(ally,enemy) = fitness(individual)
	selisih_fitness = enemy - ally

	return selisih_fitness           

def initPopulation(chess_pieces,size):
	population = []
	for i in range(0,size):
		individual = copy.deepcopy(chess_pieces)
		individual = generate_random_solution(individual)
		population.append(individual)
	return population

def reproduce(parent1,parent2):
	n = len(parent1)
	c = randint(1,n-1)

	p1 = copy.deepcopy(parent1)
	p2 = copy.deepcopy(parent2)

	p1 = sorted(p1, key=urutX)

	listp2done = []

	i = 0
	banyaktertukar = 0
	while (banyaktertukar<c and i<n):
		for piece1 in p1:
			j=0
			for piece2 in p2:
				if (str(piece1)==str(piece2) and not(isitDone(listp2done,j))):
					if (find_chess_piece(p1,piece2.x,piece2.y)==None and find_chess_piece(p2,piece1.x,piece1.y)==None):
						tempx = piece1.x
						tempy = piece1.y
						piece1.x = piece2.x
						piece1.y = piece2.y
						piece2.x = tempx
						piece2.y = tempy
						listp2done.append(j)
						banyaktertukar +=1
						break
				j+=1
			if (banyaktertukar>=c):
				break

			i+=1
	return [mutasi(p1),mutasi(p2)]

def urutX(bidak):
	return bidak.x

def isitDone(listdone, i):
	for done in listdone:
		if (done==i):
			return True
	return False

def mutasi(individual):
	generate_move_random(individual)
	return individual
