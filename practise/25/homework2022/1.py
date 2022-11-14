def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)




for x in range(174457, 174505):
    if len(div(x)) == 2:
        print(*div(x))
    
    