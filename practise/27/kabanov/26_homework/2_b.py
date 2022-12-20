f = open('27A.txt')
n = int(f.readline())
k = k_7 = 0
for i in range(n):
    x = int(f.readline())
    if x%7==0:
        k_7+=1
    else:
        k+=1
print(k_7*k + k_7*(k_7-1)/2)