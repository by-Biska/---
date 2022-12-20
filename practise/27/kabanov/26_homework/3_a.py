from itertools import combinations

f = open('27A.txt')
n = int(f.readline())
k = 0
a = [int(x) for x in f]
for j,i in combinations(a, 2):
    if j*i%65==0:
        k+=1
print(k)