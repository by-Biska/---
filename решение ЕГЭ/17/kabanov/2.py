a = [int(x) for x in open('17.txt')]

ans = [x for x in a if x % 10 == 3 or x % 10 == 5]

print(len(ans), max(ans))