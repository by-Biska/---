a = [int(x) for x in open('17 (16).txt')]
ans = []
krat17 = []
krat11 = []

for i in a:
    if i % 11 == 0 and i != 0:
        krat11.append(i)
    if i % 17 == 0 and i != 0:
        krat17.append(i)

if len(krat11) > len(krat17):
    print(len(krat11), min(krat11))
else:
    print(len(krat17), min(krat17))
