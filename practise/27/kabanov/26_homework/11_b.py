f = open('27B_5.txt')
n = int(f.readline())

k = []
k_31 = []

for i in range(n):
    x = int(f.readline())
    if x % 31 == 0:
        k_31.append(x)
    else:
        k.append(x)
k.sort()
k_31.sort()
# print(k_31[0]*k[0])
print(min(k_31[0]*k[0], k_31[0]*k_31[1]))