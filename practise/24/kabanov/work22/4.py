# import fnmatch

s = open('24 (2).txt').readline()

k = 0 
# OPTION 1
# for i in range(len(s)-3):
# 	if fnmatch.fnmatch(s[i:i+4], 'A?EX'):
# 		k += 1

# print(k)

# OPTION 2
# for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
# 	s1 = 'A'+c+'EX'
# 	k += s.count(s1)
# print(k)

# OPTION 3
for i in range(len(s) - 3):
	if s[i] + s[i+2] + s[i+3] == "AEX":
		k+= 1
print(k)