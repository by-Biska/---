for c1 in '0123456789':
    a=int(f'345789{c1}')
    if a%169 == 0:
        print(a, a//169)

for c1 in '0123456789':
    for c2 in '0123456789':
        a=int(f'345{c1}789{c2}')
        if a%169 == 0:
            print(a, a//169)

for c1 in '0123456789':
    for c2 in '0123456789':
        for c3 in '0123456789':
            a=int(f'345{c1}{c2}789{c3}')
            if a%169 == 0:
                print(a, a//169)