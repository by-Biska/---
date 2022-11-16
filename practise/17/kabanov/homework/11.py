a = [int(x) for x in open('17 (11).txt')]
ans = []

for i in range(len(a) - 3):
    if (a[i] > a[i + 1] > a[i + 2] > a[i + 3]) and a[i] - a[i + 3] > 1000:
        # print(a[i] , a[i + 1] , a[i + 2] , a[i + 3.py])
        ans.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3])
print(len(ans), min(ans))
