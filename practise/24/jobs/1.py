# s = open('24-1.txt').readline()
s = 'CKBBBKN'
prev = s[0]
m_len, c_len = 0, 1
char = ''

for i in range(1, len(s)):
	if s[i] == s[i-1]:
		c_len += 1
	else:
		if prev == s[i]:
			if m_len <= c_len:
				m_len = c_len
				char = s[i-1]
		prev = s[i-1]
		c_len = 1
print(char, m_len)