from itertools import product as pr

k = 0
for x in pr('APBUS', repeat=6):
    s = ''.join(x)
    if s.count('A') == 3:
        if (s[0] == 'A' and s[1] == 'A' and s[2] != 'A') or \
                (s[1] == 'A' and s[2] == 'A' and s[3] != 'A' and s[0] != 'A') or \
                (s[2] == 'A' and s[3] == 'A' and s[4] != 'A' and s[1] != 'A') or \
                (s[3] == 'A' and s[4] == 'A' and s[5] != 'A' and s[2] != 'A') or \
                (s[4] == 'A' and s[5] == 'A' and s[3] != 'A'):
            k += 1
print(k)
