with open('24var01.txt') as f:
    s = f.readline()

    s = s.replace('B', "*").replace('C', "*").replace('D', "*").replace('E', "*")

    count_max = count = count_A = 0

    for i in s:
        if i == '*':
            count += 1
            count_max = max(count, count_max)
        else:
            count += 1
            count_A += 1
            if count_A > 3:
                count_A = count = 0
print(count_max)
