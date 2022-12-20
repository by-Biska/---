f = open('27A_10.txt')
n = int(f.readline())

k = [0] * 100
for i in range(n):
    x = int(f.readline())
    a = sum(map(int, str(x)))
    k[a] += 1
print(max(k))
