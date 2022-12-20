from math import factorial

f = open('27B.txt')
n = int(f.readline())
k_19 = 0
for i in range(n):
    x = int(f.readline())
    if x%19==0:
        k_19+=1
print(factorial(k_19)//(factorial(3)*factorial(k_19-3)))