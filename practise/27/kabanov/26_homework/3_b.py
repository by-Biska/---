f = open('27B.txt')
n = int(f.readline())
k = k_13 = k_5 = k_65 = 0

for i in range(n):
    x = int(f.readline())
    if x % 65 == 0:
        k_65 += 1
    elif x % 13 == 0:
        k_13 += 1
    elif x % 5 == 0:
        k_5 += 1
    else:
        k += 1
print(k_65*(k+k_13+k_5) + k_65*(k_65-1)//2 + k_13*k_5)
