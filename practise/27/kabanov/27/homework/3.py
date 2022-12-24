f = open('27A.txt')
n = int(f.readline())

k1 = k0 = k5_1 = k5_0 = 0

for i in range(n):
    x = int(f.readline())

    if x % 5 == 0 and x%2 == 0: k5_0 += 1
    if x % 5 == 0 and x%2 != 0: k5_1 += 1
    if x % 5 != 0 and x%2 == 0: k0 += 1
    if x % 5 != 0 and x%2 != 0: k1 += 1

print(k5_0*k5_1+k5_0*k1+k5_1*k0)
