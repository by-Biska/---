f = open('27A_7.txt')
n = int(f.readline())
q = [int(f.readline()) for _ in range(5)]

pair = 0
k1 = k3 = k7 = k9 = 0

for _ in range(n - 5):
    x = int(f.readline())
    if x%10 == 1: pair += k3
    if x%10 == 3: pair += k1
    if x%10 == 7: pair += k9
    if x%10 == 9: pair += k7


    if q[0]%10==3:k3+=1
    if q[0]%10==7:k7+=1
    if q[0]%10==9:k9+=1
    if q[0]%10==1:k1+=1
    q.append(x)
    q.pop(0)
print(pair)
