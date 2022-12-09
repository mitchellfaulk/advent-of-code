f = open('8.txt')

M = [[int(char) for char in line.strip()] for line in f]
m = len(M)
n = len(M[0])

DIR = [(1,0), (0,1), (-1,0), (0,-1)]

ans1 = 0
ans2 = 0

for i in range(m):
	for j in range(n):
		height = M[i][j]
		is_vis = False
		full_score = 1
		for di, dj in DIR:
			ii = i
			jj = j
			ok = True
			score = 0
			while True:
				ii += di
				jj += dj
				if not (0 <= ii < m and 0 <= jj < n):
					break
				score += 1
				if M[ii][jj] >= height:
					ok = False
					break
			full_score *= score
				
			if ok: # if we make it through a direction, then change is_vis to True
				is_vis = True
		ans1 += int(is_vis)
		ans2 = max(ans2, full_score)

print(ans1, ans2)
