f = open('3.txt')

d = {}

chars = ['0','1']
positions = range(12)

for char in chars:
	for position in positions:
		d[(char, position)] = 0

for line in f:
	num = line.strip()
	for pos in range(12):
		char = num[pos]
		print(char, pos)
		d[(char, pos)] += 1

gamma = ''
epsilon = ''
for position in range(12):
	if d[('1', position)] > d[('0', position)]:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'

print(gamma, epsilon)
print(int(gamma, 2) * int(epsilon, 2))



	

