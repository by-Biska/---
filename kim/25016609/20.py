def f(s, c, m, z):
    if s >= 51: return c % 2 == m % 2
    if c == m: return 0

    h = []
    if z-1>=0: h+=[f(s+1,c+1,m,z-1)]
    if z-2>=0: h+=[f(s+2,c+1,m,z-2)]
    if z-s*2>=0: h+=[f(s+1,c+1,m,z-s*2)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 51):
    for m in range(1, 7):
        if f(s, 0, m, 60):
            print(s, m)
            break
