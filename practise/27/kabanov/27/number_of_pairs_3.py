f = open('27B.txt')
n = int(f.readline())
count = 0
k = [0]*127

for i in range(n):
    x = int(f.readline())

    ost = 0 if x%127==0 else 127-x%127
    count += k[ost]

    k[x%127] +=1
print(count)