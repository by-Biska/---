f = open('27B.txt')
n = int(f.readline())
m = float('-inf')

k = [float('-inf')] * 107
for i in range(n):
    x = int(f.readline())
    ost = 0 if x % 107 == 0 else 107 - x % 107
    m = max(x + k[ost], m)

    k[x % 107] = max(x, k[x % 107])
print(m)
