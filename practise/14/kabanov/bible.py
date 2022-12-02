x = 173
a = []
while x > 0:
    a.insert(0, x % 16)
    x //= 16
print(a)
