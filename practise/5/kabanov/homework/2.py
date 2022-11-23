for N in range(1000):
    b = bin(N)[2:]
    ans = b + "01" if N % 2 == 0 else b + "10"
    r = int(ans, 2)
    if r > 81:
        print(r)
