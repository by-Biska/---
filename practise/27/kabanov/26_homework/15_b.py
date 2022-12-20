f = open('27A_9.txt')
n = int(f.readline())

k = [[] for i in range(80)]
for i in range(n):
    x = int(f.readline())
    k[x%80]+=[x]

ans = []
for i in range(80):
    if len(k[i])>=2:
        ans += [max(k[i])- min(k[i])]
print(max(ans))