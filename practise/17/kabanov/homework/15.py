a = [int(x) for x in open('17 (15).txt')]
ans = []
max_a = max(x for x in a if x % 19 == 0)

for i in range(len(a) - 1):
    if (a[i] > max_a) or (a[i + 1] > max_a):
        ans.append(a[i] + a[i + 1])
print(len(ans), min(ans))
