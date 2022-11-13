from fnmatch import fnmatch

count = 0
for x in range(699998, 99999999, 13):
    if fnmatch(str(x), '*0??3') == False and fnmatch(str(x), '*4??2') == False and fnmatch(str(x), '*1*') == False:
        print(x)