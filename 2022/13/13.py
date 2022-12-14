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


# def compare(left_value, right_value):
# 	if left_value and not right_value:
# 		return False
# 		print('right ran out')
	
# 	if isinstance(left_value, int) and isinstance(right_value, int):
# 		if left_value > right_value:
# 			return False
# 			print('left value greater')
# 		if left_value < right_value:
# 			print('left value smaller')
# 			return True
# 	if type(left_value) is list and type(right_value) is list:
# 		if len(left_value) > len(right_value):
# 			return False
# 			print('right will run out first')
# 		else:
# 			for i in range(len(left_value)):
# 				print(left_value[i], right_value[i])
# 				if not compare(left_value[i], right_value[i]):
# 					return False
# 	if isinstance(left_value, int) and type(right_value) is list:
# 		print('convert left to list')
# 		compare([left_value], right_value)

# 	if type(left_value) is list and isinstance(right_value, int):
# 		print('convert right to list')
# 		compare(left_value, [right_value])

# 	return True


# def compare(left, right):
# 	if 

# idx = 1
# ans1 = 0
# while idx <= len(left)-1: 
# 	print(idx)
# 	if compare(left[idx], right[idx]):
# 		# print(idx)
# 		ans1 += idx
# 	idx += 1
# 	print('')

# # 6155 too high

# print(compare(left[3], right[3]))


# def compare(left, right):
# 	print('comparing', left, right)
# 	if not left:
# 		print('left ran out')
# 		return 'correct'
# 	if not right:
# 		print('right ran out')
# 		return 'wrong'
# 	while left and right:

# 		l = left.popleft()
# 		r = right.popleft()
# 		print('compare', l,r)
# 		if isinstance(l, int) and isinstance(r, int):
# 			if l == r:
# 				print('same value, so continue')
# 				continue 

# 			if l < r:
# 				print('left value smaller', l, r)
# 				return 'correct'
				
# 			if l > r:
# 				print('left value greater', l, r)
# 				return 'wrong'

# 		if type(l) is list and type(r) is list:
# 			if compare(deque(l), deque(r)) == 'same':
# 				continue
# 			else:
# 				return compare(deque(l), deque(r))
# 		if isinstance(l, int) and type(r) is list:
# 			print('change left to list')
# 			if compare(deque([l]), deque(r)) == 'same':
# 				continue
# 			else:
# 				return compare(deque([l]), deque(r))
# 		if type(l) is list and isinstance(r, int):
# 			print('change right to list')
# 			if compare(deque(l), deque([r])) == 'same':
# 				continue
# 			else:
# 				return compare(deque(l), deque([r]))
# 	return 'same'
	

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
	# print(i)
	if compare(left[i], right[i]) == 'correct':
		ans1 += i
	# print('')

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


print(sorted(d.values()))
print(len(d.values()))

for item in sorted(d, key=d.get):
	print(item, d[item])


# [[2]] at 108
# [[7]] at 219
# [[6]] at 197
# [[5]] at 180
# [[9]] at 262

# print(219*180)
# 39420 too high

print(108*197)



