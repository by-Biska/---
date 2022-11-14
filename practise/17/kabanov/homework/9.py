a = [int(x) for x in open('17.txt')]
ans = []

for i in range(len(a) - 2):
    if (abs(a[i]) % 12 == 0 or abs(a[i + 1]) % 12 == 0 \
            or abs(a[i + 2]) % 12 == 0) and abs(a[i]) % 3 == 0 \
            and abs(a[i + 1]) % 3 == 0 and abs(a[i + 2]) % 3 == 0:
        ans.append((a[i] + a[i+1] + a[i+2]) // 3)

print(len(ans), min(ans))
