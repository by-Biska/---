s = open('24.txt').readline()
s = s.replace('E', 'A').replace('U', 'A')
s = s.replace('C', 'B').replace('D', 'B').replace('F', 'B')
while 'BABAB' in s: s = s.replace('BABAB', 'BAB BAB')
s = s.replace('BAB', '*')
s = s.replace('B', ' ').replace('A', ' ')
# print(s)
print(max(len(c) for c in s.split()))