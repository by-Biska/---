f = open('27B.txt')
n = int(f.readline())
q = [int(f.readline()) for i in range(10)]
m = [[float('-inf')]*567 for i in range(2)]
ms = float('-inf')

for i in range(n-10):
    x = int(f.readline())
    ost = 0 if x%567==0 else 567-x%567
    ms = max(ms , m[x%2][ost]+x)

    m[q[0]%2][q[0]%567] = max(m[q[0]%2][q[0]%567], q[0])
    q.append(x)
    q.pop(0)
print(ms)