def f(x, A):
    return ((x % 13 == 0) <= (x % 21 != 0)) or (x + A >= 500)


for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not (f(x, A)):
            flag = False
            break
    if flag:
        print(A)
        break
