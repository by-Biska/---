f = open('27B_3.txt')
n = int(f.readline())

m = [float('inf')]*31  # min numbers
ms = float('inf')  # min sum

for i in range(n):
    x = int(f.readline())

    for y in range(31):
        if x*y%31==0: ms = min(ms, x*m[y])

    m[x%31] = min(m[x%31], x)
print(ms)