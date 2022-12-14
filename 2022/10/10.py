f = open('10.txt')

X = 1
cycle = 0
is_interesting = -20
ans1 = 0
image = ''
for line in f:
	line = line.strip().split()
	# print(line)
	if line[0] == 'noop':
		pixel = '#' if X-1 <= cycle % 40 <= X+1 else '.'
		image += pixel
		cycle += 1
		if cycle % 40 == 0:
			image += '\n'
		is_interesting += 1
		if is_interesting % 40 == 0:
			ans1 += X * cycle

			# print(cycle, X, is_interesting)
	if line[0] == 'addx':
		for _ in range(2):
			pixel = '#' if X-1 <= cycle % 40 <= X+1 else '.'
			image += pixel
			cycle += 1
			if cycle % 40 == 0:
				image += '\n'
			is_interesting += 1
			if is_interesting % 40 == 0:

				# print(cycle, X, is_interesting)
				ans1 += X * cycle
		X += int(line[1])

print(ans1) 
print(image)


