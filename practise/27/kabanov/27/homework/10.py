f = open('27B_6.txt')
n = int(f.readline())
q = [int(f.readline()) for _ in range(4)]

d = [0] * 26
pair = 0

for _ in range(n - 4):
    x = int(f.readline())
    for y in range(26):
        if (x * y) % 13 == 0 and (x + y) % 2 != 0:
            pair += d[y]
    d[q[0] % 26] += 1
    q.append(x)
    q.pop(0)
print(pair)
