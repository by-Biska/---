# with open('24.txt') as f:
#     s = f.readline()
#     s = s.replace('C', 'S').replace('D', 'S').replace('F', 'S')
#     s = s.replace('O', 'A')
#     s = s.replace('SA', '*')
#
#     k = kmax = 0
#
#     for i in s:
#         if i == '*':
#             k += 1
#             kmax = max(k, kmax)
#         else:
#             k = 0
# print(kmax)

f = open('24.txt')

for x in f:
    x = x.replace('O', 'A').replace('C', 'D').replace('F', 'D')
    print(x.count('DA' * 95))
