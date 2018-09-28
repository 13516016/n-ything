from nything import *
from util.printer import print_board, print_attacked_pieces
from random import randint
import copy
import time

def genetic(chess_pieces):
	size = 4
	population = initPopulation(chess_pieces,size)

	sortedpopulation = sorted(population, key=fitness_genetic, reverse=True)

	banyakiterasi = 100
	for i in range(0,banyakiterasi):

		sortedpopulation.extend(reproduce(sortedpopulation[0],sortedpopulation[1]))
		sortedpopulation.extend(reproduce(sortedpopulation[1],sortedpopulation[2]))

		sortedpopulation = sorted(sortedpopulation, key=fitness_genetic, reverse=True)
		sortedpopulation = sortedpopulation[:8]

	for individual in sortedpopulation:
		print_board(individual)
		print_attacked_pieces(individual)
		print('banyak bidak: '+str(len(individual)))
	print('SELESAI')
	print(time.time())

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

	arrp1 = []
	idx=0
	for eachpiece in p1:
		bidak = tuple((str(eachpiece), eachpiece.x, eachpiece.y, idx))
		arrp1.append(bidak)
		idx+=1
	arrp1 = sorted(arrp1, key=urutX)

	listp2done = []
	
	j=0
	banyaktertukar = 0

	while (banyaktertukar<c and j < n):
		i=0
		for piece2 in p2:
			if (str(p1[arrp1[j][3]])==str(piece2)):
				if not(isitDone(listp2done,i)):
					if (find_chess_piece(p1,piece2.x,piece2.y) == None and find_chess_piece(p2,p1[arrp1[j][3]].x,p1[arrp1[j][3]].y) == None):
						tempx = piece2.x
						tempy = piece2.y
						p2[i].x = p1[arrp1[j][3]].x
						p2[i].y = p1[arrp1[j][3]].y
						p1[arrp1[j][3]].x = tempx
						p1[arrp1[j][3]].x = tempy
						listp2done.append(i)
						banyaktertukar += 1
						break
			i+=1
		j += 1	


	return [mutasi(p1),mutasi(p2)]

def urutX(bidak):
	return bidak[1]

def isitDone(listdone, i):
	for done in listdone:
		if (done==i):
			return True
	return False

def mutasi(individual):
	generate_move_random(individual)
	return individual
