from itertools import combinations

f = open('27A.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 0

for x,y,z in combinations(a, 3):
    if x%19==0 and y%19==0 and z%19==0:
        k+=1
print(k)