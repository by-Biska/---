with open('24var02.txt') as f:
    s = f.readline()

    s = s.replace('B', '*').replace('C', '*').replace('D', '*').replace('E', '*')

    count_A = count = 0
    count_min = 999999999999

    len_s = len(s)

    for n in range(0, len_s):
        s = s[n:]

        for i in s:
            if i == "*":
                count += 1
            else:
                count_A += 1
                count += 1
                if count_A == 35:
                    count_min = min(count, count_min)
                    count_A = count = 0
print(count_min)
