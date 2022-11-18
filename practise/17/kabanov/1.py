a = [int(x) for x in open('17.txt')]
ans = [x for x in a if x % 3 == 0 and x%7!=0 and x%17!= 0 and x%19 != 0 and x%27 != 0]

print(len(ans), max(ans))
