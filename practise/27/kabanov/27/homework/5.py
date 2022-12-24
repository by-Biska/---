f = open('27B.txt')
n = int(f.readline())
count = 0
k = [0]*80
k50000 = [0]*80

for i in range(n):
    x = int(f.readline())

    ost = 0 if x%80==0 else 80-x%80

    if x>50_000: count+=k[ost]
    else: count+=k50000[ost]

    k[x%80]+=1
    if x>50000: k50000[x%80]+=1
print(count)