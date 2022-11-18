s = open('24 (5).txt').readline()
while 'XXXXX' in s: s = s.replace('XXXXX', 'XXXX XXXX')

print(s.count('XXXX'))