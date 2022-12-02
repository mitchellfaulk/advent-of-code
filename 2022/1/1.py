elves = []
elf = 0

with open('1.txt') as f:
	for line in f:
		if line == '\n':
			elves.append(elf)
			elf = 0
			continue

		else: 
			num = int(line)
			elf += num

elves.sort()

print(elves[-1], elves[-1] + elves[-2] + elves[-3])