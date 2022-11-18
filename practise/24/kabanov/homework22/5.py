s = open('24 (4).txt').readline()
while 'XIXIX' in s: s = s.replace('XIXIX', 'XIX XIX')

print(s.count("XIX"))