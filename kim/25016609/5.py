ans = []
for n in range(1, 16):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '1'
    else:
        b = '11' + b[2:] + '0'
    r = int(b, 2)
    ans.append(r)
print(max(ans))
