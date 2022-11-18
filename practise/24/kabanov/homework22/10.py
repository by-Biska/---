k = 0
for s in open("24 (8).txt"):
    if s.count("B") >= s.count("A") * 1.05:
        k += 1
print(k)
