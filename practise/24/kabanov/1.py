s = open('24.txt').readline()

s = s.replace("A", ' ')
s = s.replace("C", ' ')
s = s.split()
print(len(max(s, key=len)))