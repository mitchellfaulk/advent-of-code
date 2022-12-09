f = open('9.txt') # input file
DIR = {'R': (1,0), 'D': (0,-1), 'L': (-1,0), 'U': (0,1)}
rope = []
d = [] # keep track of where each knot of the rope visits
length = 10 # number of knots in the rope


for _ in range(length): #start each knot at the origin
	rope.append([0,0])
	d.append({(0,0):1})

def tug(h,t): # define a function to tug each knot behind the proceeding
	hx, hy = h
	tx, ty = t
	dx = hx - tx
	dy = hy - ty
	dist = max(abs(dx), abs(dy))
	if dist <= 1:
		return t
	else:
		if dx == 0 or dy == 0:
			t[0] += dx//2
			t[1] += dy//2
			return t
		else:
			dx = abs(dx)//dx
			dy = abs(dy)//dy
			t[0] += dx
			t[1] += dy
			return t

for line in f:
	dir, num = line.strip().split()
	num = int(num)
	dx, dy = DIR[dir]
	for _ in range(num):
		rope[0][0] += dx
		rope[0][1] += dy

		if tuple(rope[0]) not in d[0]:
			d[0][tuple(rope[0])] = 1

		for i in range(1, length):
			rope[i] = tug(rope[i-1], rope[i])
			if tuple(rope[i]) not in d[i]:
				d[i][tuple(rope[i])] = 1


ans1 = len(d[1])
ans2 = len(d[length-1])

print(ans1, ans2)		




