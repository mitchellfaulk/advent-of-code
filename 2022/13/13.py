import ast
from collections import deque

f = open('13.txt')

num = 0
left = [[]]
right = [[]]

for line in f:
	line = line.strip()
	if line:
		lst = ast.literal_eval(line)

	if num % 3 == 0:
		left.append(lst)
	if num % 3 == 1: 
		right.append(lst)
	num += 1
	

def compare(left, right):
	#print('Compare', left, right)
	if isinstance(left, int) and isinstance(right, int):
		if left < right:
			#print('left side is smaller, so correct')
			return 'correct'
		if left > right:
			#print('right side is smaller, so wrong')
			return 'wrong'
		else:
			return 'same'
	if type(left) is list and type(right) is list:
		left = deque(left)
		right = deque(right)
		while left and right:
			l = left.popleft()
			r = right.popleft()
			status = compare(l, r)
			if status == 'same':
				continue
			else:
				return status
		if not left and right:
			#print('left side ran out first, so correct')
			return 'correct'
		if not right and left:
			#print('right side ran out first, so wrong')
			return 'wrong'
		return 'same'
	if isinstance(left, int) and type(right) is list:
		left = [left]
		return compare(left, right)
	if type(left) is list and isinstance(right, int):
		right = [right]
		return compare(left, right)



ans1 = 0
for i in range(1, len(left)):
	if compare(left[i], right[i]) == 'correct':
		ans1 += i

print(ans1)


# part 2
left = left[1:]
right = right[1:]

all_packets = left + right

all_packets.append([[2]])
all_packets.append([[6]])

d = {}

for packet in all_packets:
	num_correct = 0
	for neighbor in all_packets:
		if neighbor == packet:
			continue
		else:
			if compare(neighbor, packet) == 'correct':
				num_correct += 1
	key = str(packet)
	d[key] = num_correct + 1


print(d['[[2]]']*d['[[6]]'])