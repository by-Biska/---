from fnmatch import fnmatch

count = 0
for x in range(699998+13, 99999999, 13):
    if fnmatch(str(x), '*0??3.py*') == False and fnmatch(str(x), '*4??2') == False and fnmatch(str(x), '*1*') == False:
        print(x, sum(map(int, str(x))))
        count += 1
        if count == 5:
            break