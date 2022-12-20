from itertools import combinations
f = open('27A_2.txt')
n = int(f.readline())
k = 0
a = [int(x) for x in f]
for x, y in combinations(a, 2):
    if ((x>50000 or y>50000) and (x+y)%80 == 0):
        k += 1
print(k)
