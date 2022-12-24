f = open('27B.txt')
n = int(f.readline())
count = 0
k = k3 = k5 = k15 = 0

for i in range(n):
    x = int(f.readline())
    if x % 15 == 0:
        count += k
    elif x % 5 == 0:
        count += k3
    elif x % 3 == 0:
        count += k5
    else:
        count += k15

    k += 1
    if x % 3 == 0: k3 += 1
    if x % 5 == 0: k5 += 1
    if x % 15 == 0: k15 += 1
print(count)
