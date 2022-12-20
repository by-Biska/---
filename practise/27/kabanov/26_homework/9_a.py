from itertools import *

f = open('27B_3.txt')

n = int(f.readline())

a = [int(i) for i in f if int(i)<2000]

k = 0

for i,v in combinations(a,2):

    if (i+v) == 2000:

        k+=1

print(k)
