s = open("24.txt").readline()

k = 0

for i in range(len(s) - 3):
    if s[i : i + 4] == "AVIE":
        k += 1
print(k)
