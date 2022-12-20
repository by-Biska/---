f = open('27B.txt')
n = int(f.readline())
k_0 = k_1 = 0
for i in range(n):
    x = int(f.readline())
    if x%2==0:
        k_0+=1
    else:
        k_1+=1
print((k_0*(k_0-1))//2 + (k_1*(k_1-1))//2)
