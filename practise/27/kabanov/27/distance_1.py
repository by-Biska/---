f = open('27B.txt')
n = int(f.readline())
q = [int(f.readline()) for i in range(7)]
count = 0
k = [0]*999
for i in range(n-7):
    x = int(f.readline())
    count += k[x%999]

    k[q[0]%999]+=1
    q.append(x)
    q.pop(0)
print(count)