def F(n):
    if n > 1:
        F(n - 3)
        F(n // 2)
        print(n)


F(4)