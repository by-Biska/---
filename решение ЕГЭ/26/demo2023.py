f = open('26.txt')
n = int(f.readline())
a = [int(s) for s in f]
a.sort(reverse=True)
print(a[:10])
count = 1
s = a[0]
for i in range(1, len(a)):
    if s - a[i] >= 3:
        count += 1
        s = a[i]
print(count, s)
