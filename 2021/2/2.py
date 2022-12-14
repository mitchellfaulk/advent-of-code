f = open('2.txt')

h = 0
d = 0

for line in f:
	x, y = line.strip().split()
	y = int(y)
	if x[0] == 'f':
		h += y
	elif x[0] == 'd':
		d += y
	else:
		d -= y
print(h*d)

# part 2
h, d, a = 0, 0, 0 

f = open('2.txt')
for line in f:
	x, y = line.strip().split()
	y = int(y)
	if x[0] == 'f':
		h += y
		d += a * y
	elif x[0] == 'd':
		a += y
	else:
		a -= y

print(h*d)

