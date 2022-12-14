f = open('11.txt')

levels = []


# read the data into the levels list
count = 0 
for line in f:
	line = line.strip().split()
	# print(line)
	if line and line[0] == 'Starting':
		levels.append([])
		for item in line[2:]:
			num = int(item.strip(','))
			levels[count].append(num)
		count += 1

# define monkey operations
def do_op(item, idx):
	if idx == 0:
		return item * 11
	elif idx == 1:
		return item + 1
	elif idx == 2:
		return item + 6
	elif idx == 3: 
		return item * item
	elif idx == 4:
		return item * 7
	elif idx == 5:
		return item + 8
	elif idx == 6:
		return item + 5
	else: 
		return item + 7

# define tests
def test(num, idx):
	if idx == 0:
		levels[7].append(num) if num % 2 == 0 else levels[4].append(num)
	elif idx == 1:
		levels[3].append(num) if num % 13 == 0 else levels[6].append(num)
	elif idx == 2:
		levels[1].append(num) if num % 3 == 0 else levels[6].append(num)
	elif idx == 3:
		levels[7].append(num) if num % 17 == 0 else levels[0].append(num)
	elif idx == 4:
		levels[5].append(num) if num % 19 == 0 else levels[2].append(num)
	elif idx == 5:
		levels[2].append(num) if num % 7 == 0 else levels[1].append(num)
	elif idx == 6:
		levels[3].append(num) if num % 11 == 0 else levels[0].append(num)
	else:
		levels[4].append(num) if num % 5 == 0 else levels[5].append(num)


# part 1

d = {}
for i in range(len(levels)):
	d[i] = 0


for _ in range(20):
	for i in range(len(d)):
		# print(i, len(levels[i]))
		d[i] += len(levels[i])
		while levels[i]:
			level = levels[i].pop()
			# print(level)
			level = do_op(level, i)
			level = level //3
			test(level,i)


inspections = list(d.values())
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])


# part 2

f = open('11.txt')

# reset the levels list
levels = []

# read the data into the levels list
count = 0 
for line in f:
	line = line.strip().split()
	# print(line)
	if line and line[0] == 'Starting':
		levels.append([])
		for item in line[2:]:
			num = int(item.strip(','))
			levels[count].append(num)
		count += 1

# reset the dictionary
for i in range(len(levels)):
	d[i] = 0

# define the least common multiple of the primes appearing in the tests
modulus = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

for _ in range(10000):
	for i in range(len(d)):
		# print(i, len(levels[i]))
		d[i] += len(levels[i])
		while levels[i]:
			level = levels[i].pop()
			# print(level)
			level = do_op(level, i)
			level %= modulus
			test(level,i)

inspections = list(d.values())
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])



# 15310845153
	


