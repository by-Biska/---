f = open('27A_2.txt')
n = int(f.readline())

m = [float('-inf')] * 2  # max numbers
for _ in range(n):
    x = int(f.readline())
    m[x % 2] = max(x, m[x % 2])
print(m[0]+m[1])
