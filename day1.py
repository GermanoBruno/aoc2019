from functools import reduce

def soma(x, y):
	return (x+y)
def mass(x):
	return (int(x / 3) - 2)

def getData(filename):
	with open(filename) as f:
		lines = f.readlines()
	lista = []
	for line in lines:
		lista.append(int(line))
	f.close()
	return lista

numbers = getData('day1data.txt')
#numbers = [14, 1969, 100756]
numbers = list(map(mass, numbers))

print(reduce(soma, numbers))