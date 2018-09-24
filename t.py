import copy

def func(l1):
	l1[0] = 999
	return

def main():
	l1 = [1,2,3,4,5]
	print(l1)
	func(l1)
	print(l1)

main()

