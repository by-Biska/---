s = open('24 (3).txt').readline()
while "JBOSSJBOSSJ" in s: s = s.replace('JBOSSJBOSSJ', 'JBOSSJ JBOSSJ')
print(s.count('BOSS')-s.count('JBOSS')-s.count('BOSSJ')+s.count('JBOSSJ'))