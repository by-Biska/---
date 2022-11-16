s = open('24 (13).txt').readline()

m = ''

s = s.split('A')

for i in range(len(s)-1):
    sub = s[i]+"A"+s[i+1]
    m = max(m,sub, key=len)
print(m, len(m))