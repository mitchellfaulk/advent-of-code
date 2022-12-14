f = open('12.txt')

# create a matrix of heights
H = []

# initialize a matrix to contain the minimal number of steps to that grid position
M = []

for line in f:
	row = []
	steps = []
	line = line.strip()
	for char in line:
		if char == 'S':
			height = -1
		elif char == 'E':
			height = 26
		else:
			height = ord(char) - ord('a')
		row.append(height)
		steps.append(-1)
		
	H.append(row)
	M.append(steps)

# create a dictionary {minimal steps from start as an int -> those positions at that minimal distance as a list}
d = {}

# find the starting position and add it to d[0]
# also find the ending position and label those grid indices as Ei, Ej

for i in range(len(H)):
	for j in range(len(H[0])):
		if H[i][j] == -1:
			d[0] = [[i,j]]
			M[i][j] = 0
		if H[i][j] == 26:
			Ei = i
			Ej = j

# DIR for right, up, left, down
DIR = [(1,0), (0,1), (-1, 0), (0,-1)]


# working in order of increasing minimal steps from the start, 
# add positions to the dictionary and change the corresponding
# value in the matrix M to have the minimal steps from the start

steps = 0
while d[steps]:
	d[steps+1] = []
	for position in d[steps]:
		i, j = position
		elevation = H[i][j]
		for di, dj in DIR:
			ii = i + di
			jj = j + dj
			if 0 <= ii <= len(H)-1 and 0 <= jj <= len(H[0])-1:
				if M[ii][jj] == -1 and H[ii][jj] <= elevation + 1:
					M[ii][jj] = steps + 1
					d[steps+1].append([ii,jj])

	steps += 1


print(M[Ei][Ej])




# part 2

# change M back to -1s

for i in range(len(H)): 
	for j in range(len(H[0])):
		M[i][j] = -1

# initialize d again to be empty

d = {}

# change all occurences of 'S' or 'a' to a zero in M and add them to the dictionary

d[0] = []
for i in range(len(H)):
	for j in range(len(H[0])):
		if H[i][j] == -1 or H[i][j] == 0:
			d[0].append([i,j])
			M[i][j] = 0


steps = 0
while d[steps]:
	d[steps+1] = []
	for position in d[steps]:
		i, j = position
		elevation = H[i][j]
		for di, dj in DIR:
			ii = i + di
			jj = j + dj
			if 0 <= ii <= len(H)-1 and 0 <= jj <= len(H[0])-1:
				if M[ii][jj] == -1 and H[ii][jj] <= elevation + 1:
					M[ii][jj] = steps + 1
					d[steps+1].append([ii,jj])

	steps += 1

print(M[Ei][Ej])





