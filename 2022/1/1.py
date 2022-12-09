f = open('1.txt')
elves = []
elf = 0

for line in f:
	num = line.strip() 
	if num:
		elf += int(num)
	else:
		elves.append(elf)
		elf = 0

elves.sort(reverse=True)

ans1 = elves[0]
ans2 = sum(elves[:3])

print(ans1, ans2)