f = open('27B.txt')
n = int(f.readline())
ms = float('-inf')
m = [float('-inf')] * 350
for i in range(n):
    x = int(f.readline())
    ost = 0 if x % 350 == 0 else 350 - x % 350

    if m[ost] > x:
        ms = max(ms, m[ost] + x)

    m[x % 350] = max(m[x % 350], x)

print(ms)
