f = open('27B.txt')
n = int(f.readline())
k = [0]*69
for i in range(n):
    x = int(f.readline())
    k[x%69]+=1
count = 0
for i in range(len(k)):
    count += k[i]*(k[i]-1)//2
print(count)