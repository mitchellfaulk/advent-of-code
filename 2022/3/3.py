def getPriority(char):
	order = ord(char)
	if order > 96:
		priority = order - 96
	else:
		priority = order - 64 + 26
	return priority

total = 0

with open('3.txt') as f:
	for line in f:
		sack = line.strip()
		n = len(sack)
		comp1 = sack[:n//2]
		comp2 = sack[n//2:]
		for char in comp2:
			if char in comp1:
				priority = getPriority(char)
				# print(char, priority)
				total += priority
				break

print(total)

total = 0

with open('3.txt') as f:
	for i, line in enumerate(f):
		if i % 3 == 0:
			sack1 = line.strip()
		elif i % 3 == 1:
			sack2 = line.strip()
			shared = ''
			for char in sack2:
				if char in sack1:
					shared += char
		else:
			sack3 = line.strip()
			for char in sack3:
				if char in shared:
					priority = getPriority(char)
					# print(char, priority)
					total += priority
					break

print(total)
