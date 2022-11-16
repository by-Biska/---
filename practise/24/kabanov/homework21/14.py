s = open('24 (12).txt').readline()

ans = []

while "DD" in s: s = s.replace('DD', "D D")

s = s.split()

for i in range(len(s)):
    ans.append(len(s[i]))

# m = min(s.split(), key=len)

print(sorted(ans))
