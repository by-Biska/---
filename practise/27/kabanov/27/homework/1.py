f = open('27A.txt')
n = int(f.readline())

count = 0

k = k7 = 0

for i in range(n):
    x = int(f.readline())
    if x%7==0: count+=k
    if x%7!=0: count+=k7

    k+=1
    if x%7==0: k7+=1
print(count)