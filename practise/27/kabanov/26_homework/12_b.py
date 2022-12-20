f = open('27B_6.txt')
n = int(f.readline())

k_0, k_1, k_23_0, k_23_1 = [],[],[],[]

for i in range(n):
    x = int(f.readline())

    if x % 23 == 0 and x % 2 == 0: k_23_0.append(x)
    if x % 23 == 0 and x % 2 == 1: k_23_1.append(x)
    if x % 23 != 0 and x % 2 == 0: k_0.append(x)
    if x % 23 != 0 and x % 2 == 1: k_1.append(x)

k_23_0.sort()
k_23_1.sort()
k_0.sort()
k_1.sort()

print(max( k_23_0[-1]+k_23_0[-2], k_23_1[-1]+k_23_1[-2], k_23_0[-1]+k_0[-1], k_23_1[-1]+k_1[-1] ))