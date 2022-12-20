f = open('27B_12.txt')
n = int(f.readline())
k = [0] * 10

for i in range(n):
    x = int(f.readline())
    while x > 0:
        k[x % 10] += 1
        x //= 10

print(min(k))
# print(min(x for x in k if x != 0))
