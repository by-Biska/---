f = open('27B.txt')
n = int(f.readline())
count = 0
k = [0]*65

for i in range(n):
    x = int(f.readline())
    for j in range(65):
        if x*j%65==0: count += k[j]

    k[x%65] +=1
print(count)
