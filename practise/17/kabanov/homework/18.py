a = [int(x) for x in open('17 (18).txt')]

ans1 = []

for i in range(len(a) - 1):
    if (a[i] % 9 == 0 and a[i + 1] % 9 != 0 and abs(a[i + 1]) % 8 == 3) or \
            (a[i + 1] % 9 == 0 and a[i] % 9 != 0 and abs(a[i]) % 8 == 3):
        ans1.append(max(a[i], a[i + 1]))

print(len(ans1), max(ans1))
