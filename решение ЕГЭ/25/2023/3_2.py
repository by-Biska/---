for x in range(51, 10**6, 15):
    s = str(x)
    if s[0]+s[1] == '56' and '98' in s:
        print(x,x//51 )