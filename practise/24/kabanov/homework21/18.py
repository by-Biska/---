s = open('24 (15).txt', encoding="utf-8").readline()

# s = s.replace("КОТ", "*")
# c = m = 0
#
# for i in range(len(s)):
#     if s[i] == '*':
#         c += 1
#         m = (c,m)
#     else:
#         c = 0
# print(m)

s = s.replace("КОТ", "$").replace("К", " ").replace("О", " ").replace("Т", " ")
m = 0
for c in s.split(' '):
    m = max(m, len(c))
print(m)
