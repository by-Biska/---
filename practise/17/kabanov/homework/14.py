a = [int(x) for x in open('17 (14).txt')]
ans = []
av_a = sum(a) // len(a)

for i in range(len(a) - 2):
    if ((a[i] > av_a) + (a[i + 1] > av_a) + (a[i + 2] > av_a)) >= 2:
        ans.append(a[i] + a[i + 1] + a[i + 2])
print(len(ans), max(ans))
