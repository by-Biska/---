k = 0
for s in open("24 (10).txt"):
    while "AOAOA" in s:
        s = s.replace("AOAOA", "AOA AOA")
    while "OAOAO" in s:
        s = s.replace("OAOAO", "OAO OAO")
    if s.count("AOA") > s.count("OAO"):
        k += 1
print(k)
