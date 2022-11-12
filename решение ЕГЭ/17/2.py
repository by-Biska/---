with open('17var01.txt') as f:
    data = [int(i) for i in f]
    data_max = max(data)
    n1 = data[0]
    count = 0
    answer = []
    for i in range(1, len(data)):
        n2 = data[i]
        if n1 + n2 == data_max:
            count += 1
            answer.append(n1 ** 2 + n2 ** 2)
        n1 = n2
    print(count, max(answer))
