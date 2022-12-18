print('x w y z')
for x in range(2):
    for w in range(2):
        for y in range(2):
            for z in range(2):
                if (w<= ((x <= z) <= y)) == 0:
                    print(x,w,y,z)