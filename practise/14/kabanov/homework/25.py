for x in range(21):
	for y in range(21):
		a = 21**4 + 2*21**3 + y*21**2 + x*21 + 9 + 3*21**4 + 6*21**3 + y*21**2 + 9*21 + 9
		if a % 18 == 0:
			print(x,y,a//18)

# for x in '0123456789abcdefghijk':
# 	for y in '0123456789abcdefghijk':
# 		a = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
# 		if a % 18 ==0:
# 			print(x,y,a//18)