from model import *

def parse(filename) :
	filetest = open(filename, "r")

	arrcomponent = []

	for line in filetest :
		component = line.split(" ")
		color = component[0].lower()
		types = component[1].lower()
		n = int(component[2])
		if types == "knight" :
			knight = Knight(0, 0, color)
			for i in range (0, n) :
				arrcomponent.append(knight)
		elif types == "bishop" :
			bishop = Bishop(0, 0, color)
			for i in range (0, n) :
				arrcomponent.append(bishop)
		elif types == "rook" :
			rook = Rook(0, 0, color)
			for i in range (0, n) :
				arrcomponent.append(rook)
		elif types == "queen" :
			queen = Queen(0, 0, color)
			for i in range (0, n) :
				arrcomponent.append(queen)

	filetest.close()

	return arrcomponent