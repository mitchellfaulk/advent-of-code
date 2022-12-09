path = [] # keep track of the path to the current directory
SZ = {} # dictionary {path_name => size}
f = open('7.txt') # input

for line in f:
	words = line.strip().split()
	if words[1] == 'cd':
		if words[2] == '/':
			path = ['root']
		elif words[2] == '..':
			path.pop()
		else:
			path.append(words[2])
	elif words[1] == 'ls' or words[0] == 'dir':
		continue
	else:
		sz = int(words[0])
		for i in range(len(path)):
			parent_path = '/'.join(path[:i+1]) # add file size to ALL parent paths
			if parent_path not in SZ:
				SZ[parent_path] = sz
			else:
				SZ[parent_path] += sz

need = 3e7 - (7e7 - SZ['root'])

ans1 = 0
ans2 = 7e7

for path_name in SZ:
	if SZ[path_name] <= 100000:
		ans1 += SZ[path_name]
	if SZ[path_name] >= need:
		ans2 = min(ans2, SZ[path_name])
	

print(ans1, ans2)









