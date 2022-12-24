f = open('27B.txt')
n = int(f.readline())

k = [0]*131
count = 0
for i in range(n):
    x = int(f.readline())

    ost = 0 if x%131 == 0 else 131-x%131
    count += k[ost]

    k[x%131]+=1
print(count)