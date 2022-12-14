f = open('1.txt') 

ans1, ans2 = 0, 0
nums = []
for line in f:
	num = int(line.strip())
	nums.append(num)

for i in range(len(nums)-2):
	if nums[i+1] > nums[i]:
		ans1 += 1
	if sum(nums[i+1:i+4]) > sum(nums[i:i+3]):
		ans2 += 1

print(ans1, ans2)
