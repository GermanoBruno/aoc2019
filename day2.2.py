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
		intcode = None
	return intcode

def programReader(program):
	instrPos = 0
	opcode = program[0]
	while opcode != 99:
		program = readInstruction(program, instrPos)
		if program == None:
			return None
		instrPos += 4
		opcode = program[instrPos]
	return program

terms = list(range(0, 100))

#program = [1,1,1,4,99,5,6,0,99]
for noun in terms:
	for verb in terms:
		program = getData('day2data.txt')
		program[1] = noun
		program[2] = verb
		program = programReader(program)

		if program != None and program[0] == 19690720:
			print((100*noun) + verb)

print(program[0])