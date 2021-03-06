def getData(filename):
	lista = []
	with open(filename) as f:
		numbers = f.read()
	f.close()
	numbers = numbers.split(',')
	for number in numbers:
		lista.append(int(number))
	return lista

def readInstruction(intcode, opCodePos):
	if intcode[opCodePos] == 1:
		#num da posicao + 3 recebe +2 + +1
		intcode[intcode[opCodePos + 3]] = intcode[intcode[opCodePos + 1]] + intcode[intcode[opCodePos + 2]]
	elif intcode[opCodePos] == 2:
		#num da posicao + 3 recebe +2 * +1
		intcode[intcode[opCodePos + 3]] = intcode[intcode[opCodePos + 1]] * intcode[intcode[opCodePos + 2]]
	else:
		print("Op fail\nOpcode = " + str(intcode[opCodePos]))
	return intcode

def programReader(program):
	instrPos = 0
	opcode = program[0]
	while opcode != 99:
		program = readInstruction(program, instrPos)
		instrPos += 4
		opcode = program[instrPos]
	return program

#program = [1,1,1,4,99,5,6,0,99]
program = getData('day2data.txt')
program[1] = 12
program[2] = 2
program = programReader(program)

print(program[0])