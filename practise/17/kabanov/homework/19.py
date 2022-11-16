a = [int(x) for x in open('17 (19).txt')]

ans = []

for i in range(len(a) - 2):
    if not (a[i] > 0 and abs(a[i]) % 10 == 9) and \
            (a[i + 1] > 0 and abs(a[i + 1]) % 10 == 9) and \
            not (a[i + 2] > 0 and abs(a[i + 2]) % 10 == 9):
        ans.append(a[i] + a[i + 1] + a[i + 2])

print(len(ans), max(ans))
