s = "XXYZZYXZYYZXYZZYZXY"
maxi = 0
cur = ''
for start in range(3):
    s1 = s[start:]
    i = 0
    cur = ''
    while i + 2 < len(s1):
        if s1[i] in "XZ" and s1[i + 2] == "Y":
            cur += s[i:i + 3]
            maxi = max(len(cur), maxi)
        else:
            cur = ''
        i += 3
print(maxi // 3)
