f = open('27A_5.txt')
n = int(f.readline())
q = [int(f.readline()) for x in range(8)]

pair = 0
k = [0] * 23

for i in range(n - 8):
    x = int(f.readline())
    for y in range(23):
        if x * y % 23 == 0:
            pair += k[y]
    k[q[0] % 23] += 1
    q.append(x)
    q.pop(0)
print(pair)
