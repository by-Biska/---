s = 124*'2' + 19*'1'
while '222' in s or '111' in s:
	if '222' in s: s = s.replace('222', '1', 1)
	if '111' in s: s = s.replace('111', '2', 1)
print(s)