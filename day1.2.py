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

def rocketScience(x):
	print("rocketScience de " + str(x))
	m = mass(x)
	massaInicial = x
	exit = False
	while exit != True:
		print(m)
		if m >= 0:
			x = x + m
			m = mass(m)
		else:
			exit = True
	print('Final = ' + str(x - massaInicial) + ' de ' + str(massaInicial))
	return x - massaInicial

numbers = getData('day1data.txt')
#numbers = [14, 1969, 100756]
numbers = list(map(rocketScience, numbers))

print(reduce(soma, numbers))