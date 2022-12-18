s = [int(d) for d in open('17.txt')]

m = min(x for x in s if x%8==0 and x!=8)

ans = []
for i in range(len(s)-1):
    if s[i]%m==0 and s[i+1]%m==0:
        ans.append(s[i]+s[i+1])
print(len(ans), min(ans))
for i in range(len(s)-1):
    if s[i]+s[i+1] == min(ans):
        print(s[i], s[i+1])