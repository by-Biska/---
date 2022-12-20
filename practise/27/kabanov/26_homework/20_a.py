f = open('27B_14.txt')
n = int(f.readline())
x0 = y0 = k = 0

for i in range(n):
    x, y = map(int, f.readline().split())
    if x == 0:
        x0 += 1
    elif y == 0:
        y0 += 1
    else:
        k += 1
print(x0 * y0 * k)
