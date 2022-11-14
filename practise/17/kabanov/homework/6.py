a = [int(x) for x in open('17.txt')]
ans = []

for x in range(len(a)-1):
    if abs(a[x]+a[x+1]) % 3 == 0 and abs(a[x]+a[x+1]) % 6 != 0 and abs(a[x]*a[x+1]) % 10 == 8:
        ans.append(a[x]+a[x+1])

print(len(ans), max(ans))