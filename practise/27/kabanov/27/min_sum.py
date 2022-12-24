f = open('27B.txt')
n = int(f.readline())
ms = m = m17 = float('inf')

for i in range(n):
    x = int(f.readline())
    if x % 17 == 0:
        ms = min(x + m, ms)
    else:
        ms = min(x + m17, ms)

    m = min(x, m)
    if x % 17 == 0: m17 = min(x, m17)
print(ms)
