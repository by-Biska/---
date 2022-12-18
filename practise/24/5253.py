s = open('24-208.txt').readline()
s = s.split('2022')
m = 0
for i in range(len(s) - 4):
    if i == 0:
        c = s[i] + '2022' + s[i + 1] + '2022' + s[i + 2] + '2022' + s[i + 3] + '2022' + s[i + 4] + '202'
    elif i == len(s)-5:
        c = '022' + s[i] +  '2022' + s[i + 1] + '2022' + s[i + 2] + '2022' + s[i + 3] + '2022' + s[i + 4]
    else:
        c = '022' + s[i] + '2022' + s[i + 1] + '2022' + s[i + 2] + '2022' + s[i + 3] + '2022' + s[i + 4] + '202'
    m = max(m, len(c))
print(m)
