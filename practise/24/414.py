s = open('24_3.txt').readline()
s = s.replace('RUSTEM', '#')
s = s.replace('RUS', '$')
print(s.count('$'))