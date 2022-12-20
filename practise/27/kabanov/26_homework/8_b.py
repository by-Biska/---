f = open('27B_2.txt')
n = int(f.readline())
k = [0]*80
k5 = [0]*80

for i in range(n):
    x = int(f.readline())
    if x>50000:
        k5[x%80]+=1
    else:
        k[x%80]+=1
count = 0
count += k5[0]*(k5[0]-1)//2 + k5[40]*(k5[40]-1)//2
for i in range(1, 39+1):
    count += k5[i]*k5[80-i]

count += k5[0]*k[0] + k5[40]*k[40]
for i in range(1, 39+1):
    count += k5[i]*k[80-i]
    count += k[i]*k5[80-i]
print(count)