import sys
sys.path.append('../')

from model import *

filetest = open("test1.txt", "r")

arrcomponent = []

for line in filetest :
	component = line.split(" ")
	color = component[0].lower()
	types = component[1].lower()
	print(component[0])
	print(component[1])
	print(component[2])
	n = int(component[2])
	if types == "knight" :
		knight = Knight(int(0), int(0), color)
		for i in range (0, n) :
			arrcomponent.append(knight)
	elif types == "bishop" :
		bishop = Bishop(int(0), int(0), color)
		for i in range (0, n) :
			arrcomponent.append(bishop)
	elif types == "rook" :
		rook = Rook(int(0), int(0), color)
		for i in range (0, n) :
			arrcomponent.append(rook)
	elif types == "queen" :
		queen = Queen(int(0), int(0), color)
		for i in range (0, n) :
			arrcomponent.append(queen)

print()

for each in arrcomponent :
	print(each.x,'',each.y,'',each.color)