a = [int(x) for x in open('17 (20).txt')]

sum_a = [x for x in a if x % 35 == 0]
ans1 = []
ans = []

print(sum_a)
for x in sum_a:
    while x > 0:
        s = x % 10
        ans1.append(s)
        x = x // 10
sum_a1 = sum(ans1)
for i in range(len(a) - 1):
    if (a[i] > sum_a1 and a[i+1] <= sum_a1 and \
            hex(a[i+1])[-2] == "e" and hex(a[i+1])[-1] == "f") or \
            (a[i+1] > sum_a1 and a[i] <= sum_a1 and \
            hex(a[i])[-2] == "e" and hex(a[i])[-1] == "f"):
        ans.append(a[i] + a[i + 1])

print(len(ans), min(ans))
