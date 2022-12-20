f = open('27B_11.txt')
n = int(f.readline())

k = [0]*9

for i in range(n):
    x = int(f.readline())
    a = int(str(x)[0])
    k[a-1]+=1
print(min(k))