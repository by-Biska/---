f = open('27B.txt')
n = int(f.readline())
k_5_0 = k_5_1 = k_0 = k_1 = 0

for i in range(n):
    x = int(f.readline())
    if x%5==0 and x%2==0: k_5_0+=1
    if x%5==0 and x%2==1: k_5_1+=1
    if x%5!=0 and x%2==0: k_0+=1
    if x%5!=0 and x%2==1: k_1+=1
print(k_5_1*k_0 + k_5_0*k_1 + k_5_1*k_5_0)