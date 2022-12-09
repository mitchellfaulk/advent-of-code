# part 1

stacks = [
    ['z', 't', 'f', 'r', 'w', 'j', 'g'],
    ['g', 'w', 'm'],
    ['j', 'n', 'h', 'g'],
    ['j', 'r', 'c', 'n', 'w'],
    ['w', 'f', 's', 'b', 'g', 'q', 'v', 'm'],
    ['s', 'r', 't', 'd', 'v', 'w', 'c'],
    ['h', 'b', 'n', 'c', 'd', 'z', 'g', 'v'], 
    ['s', 'j', 'n', 'm', 'g', 'c'],
    ['g', 'p', 'n', 'w', 'c', 'j', 'd', 'l']
]

with open('5.txt') as f:
	for line in f:
		lst = line.split()
		count = int(lst[1])
		start = int(lst[3]) - 1
		end = int(lst[5]) - 1
		for _ in range(count):
			stacks[end].append(stacks[start].pop())

ans = ''
for i in range(len(stacks)):
	ans += stacks[i].pop()

print(ans.upper())



# part 2

stacks = [
    ['z', 't', 'f', 'r', 'w', 'j', 'g'],
    ['g', 'w', 'm'],
    ['j', 'n', 'h', 'g'],
    ['j', 'r', 'c', 'n', 'w'],
    ['w', 'f', 's', 'b', 'g', 'q', 'v', 'm'],
    ['s', 'r', 't', 'd', 'v', 'w', 'c'],
    ['h', 'b', 'n', 'c', 'd', 'z', 'g', 'v'], 
    ['s', 'j', 'n', 'm', 'g', 'c'],
    ['g', 'p', 'n', 'w', 'c', 'j', 'd', 'l']
]

with open('5.txt') as f:
	for line in f:
		lst = line.split()
		count = int(lst[1])
		start = int(lst[3]) - 1
		end = int(lst[5]) - 1
		temp = []
		for _ in range(count):
			temp.append(stacks[start].pop()) 

		for _ in range(len(temp)):
			stacks[end].append(temp.pop())

ans = ''
for i in range(len(stacks)):
	ans += stacks[i].pop()

print(ans.upper())