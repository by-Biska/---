a = [int(x) for x in open('17 (17).txt')]

ans4 =[]
ans =[]

for i in a:
    if i % 10 == 4:
        ans4.append(i)

ans4 = min(ans4) + max(ans4)

for i in range(len(a)-1):
    if a[i] + a[i + 1] < ans4:
        ans.append(a[i] + a[i + 1])

print(len(ans), max(ans))