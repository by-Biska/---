f = open('27B_3.txt')
n = int(f.readline())
k = [0]*2000

for i in range(n):
    x = int(f.readline())
    if x < 2000:
        k[x]+=1
count = 0
count += k[1000]*(k[1000]-1)//2
for i in range(1, 999+1):
    count += k[i]*k[2000-i]
print(count)