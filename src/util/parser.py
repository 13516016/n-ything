from model import *

def parse(filename) :
	with open(filename, "r") as file:
		arrcomponent = []
		for line in file :
			component = line.split(" ")
			color = component[0].lower()
			types = component[1].lower()
			n = int(component[2])
			
			if color == "black" :
				color = Color.BLACK
			else:
				color = Color.WHITE

			if types == "knight" :
				for i in range (0, n) :
					knight = Knight(-1, -1, color)
					arrcomponent.append(knight)
			elif types == "bishop" :
				for i in range (0, n) :
					bishop = Bishop(-1, -1, color)
					arrcomponent.append(bishop)
			elif types == "rook" :
				for i in range (0, n) :
					rook = Rook(-1, -1, color)
					arrcomponent.append(rook)
			elif types == "queen" :
				for i in range (0, n) :
					queen = Queen(-1, -1, color)
					arrcomponent.append(queen)

		file.close()

	return arrcomponent