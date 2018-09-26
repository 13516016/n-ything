from nything import *
from util.printer import print_board, print_attacked_pieces
from random import randint
import copy

def genetic(chess_pieces):
	size = 4
	population = initPopulation(chess_pieces,size)

	sortedpopulation = sorted(population, key=fitness_genetic, reverse=True)

	banyakiterasi = 3
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

	arrp1 = []
	idx=0
	for eachpiece in p1:
		bidak = tuple((str(eachpiece), eachpiece.x, eachpiece.y,idx))
		arrp1.append(bidak)
		idx+=1
	arrp1 = sorted(arrp1, key=urutX)
	arrp1 = arrp1[:c]

	listp2done = []
	for idx1 in arrp1:
		i=0
		for piece2 in p2:
			if (str(p1[idx1[3]])==str(piece2)):
				if not(isitDone(listp2done,i)):
					p2[i] = p1[idx1[3]]
					p1[idx1[3]] = piece2
					listp2done.append(i)
					break
			i+=1

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
