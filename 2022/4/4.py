ans1, ans2 = 0, 0

with open('4.txt') as f:
	for line in f:
		elf1, elf2 = line.strip().split(',')
		l1, r1 = elf1.split('-')
		l2, r2 = elf2.split('-')
		l1, r1 = int(l1), int(r1)
		l2, r2 = int(l2), int(r2)
		l = min(l1, l2)
		r = max(r1, r2)
		if (l1 == l and r1 == r) or (l2 == l and r2 == r):
			ans1 += 1
		if (l2 <= r1) and (l1 <= r2):
			ans2 += 1
		
print(ans1, ans2)



