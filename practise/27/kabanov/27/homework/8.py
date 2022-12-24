f = open('27B_4.txt')
n = int(f.readline())

m0 = float('-inf')
m1 = float('-inf')
m23_0 = float('-inf')
m23_1 = float('-inf')
ms = float('-inf')

for i in range(n):
    x = int(f.readline())

    if x % 23 == 0 and x % 2 == 0:
        ms = max(x + m0, ms)
    elif x % 23 == 0 and x % 2 != 0:
        ms = max(x + m1, ms)
    elif x % 23 != 0 and x % 2 == 0:
        ms = max(x + m23_0, ms)
    elif x % 23 != 0 and x % 2 != 0:
        ms = max(x + m23_1, ms)

    if x % 2 == 0: m0 = max(m0, x)
    if x % 2 != 0: m1 = max(m1, x)
    if x % 23 == 0 and x % 2 == 0: m23_0 = max(m23_0, x)
    if x % 23 == 0 and x % 2 != 0: m23_1 = max(m23_1, x)
print(ms)
