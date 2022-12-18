s = open('24-211.txt').readline()

c = m = 0
for j in range(4):
    for i in range(j, len(s)-3, 3):
        if s[i]+s[i+1]+s[i+2]+s[i+3] in ['ABEC','BDAC','CFBA','CAFB']:
            c+=1
            m = max(m,c)
        else:
            c = 0
print(m)



# s = s.replace('ABECAFB','ABECCAFB')
# s = s.replace('ABECFBA','ABECCFBA')
# s = s.replace('BDACAFB','BDACCAFB')
# s = s.replace('BDACFBA','BDACCFBA')
# s = s.replace('CFBABEC','CFBAABEC')
# s = s.replace('CAFBDAC','CAFBBDAC')
#
# s = s.replace('ABEC', '*').replace('BDAC', '*').replace('CAFB', '*').replace('CFBA', '*')
# print(s[:1000])
# for c in 'ABCDEF': s = s.replace(c, ' ')
# print(max(len(c) for c in s.split()))