with open('6.txt') as f:
	for s in f:
		for i in range(len(s)-3):
			window1 = s[i:i+4]
			if len(window1) == len(set(window1)):
				print(i+4)
				break

with open('6.txt') as f:
	for s in f:
		for i in range(len(s) - 13):
			window2 = s[i:i+14]
			if len(window2) == len(set(window2)):
				print(i+14)
				break
