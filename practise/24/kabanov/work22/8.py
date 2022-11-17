k = 0
for s in open("24 (3).txt"):
    if s.count("J") > s.count("E"):
        k += 1
print(k)
