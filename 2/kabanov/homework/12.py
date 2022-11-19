print("w x y z")

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not w) and ((y or z) <= ((not x) and y)):
                    print(w, x, y, z)