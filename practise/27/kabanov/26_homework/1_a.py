from itertools import combinations

f = open('27A.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 0
for i, j in combinations(a, 2):
    if (i + j)%2==0:
        k+=1

print(k)