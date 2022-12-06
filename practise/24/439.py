s = open('24_4.txt').readline()

count = 0
length = 1
for i in range(1, len(s)):
	if s[i] > s[i-1]:
		length +=1
	else:
		if length == 5:
			count+=1
		length = 1
if length == 5:
	count += 1
print(count)