a = [int(x) for x in open('17.txt')]

ans = [x for x in a if (x%16 == 11 or x%16 == 13) and (x%7==0 and x%6!=0 and x%13!=0 and x%19!=0)]

print(sum(ans), len(ans))