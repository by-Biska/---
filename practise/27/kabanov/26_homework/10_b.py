f = open('27A_4.txt')
n = int(f.readline())

k_0 = []
k_1 = []

for i in range(n):
    x = int(f.readline())
    if x%2==0:
        k_0.append(x)
    else:
        k_1.append(x)
k_0.sort()
k_1.sort()

print(k_1[-1] + k_0[-1])
