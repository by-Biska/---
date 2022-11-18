k = 0
K = 0
count_A = 0
flag_A = False

# s = open("24 (11).txt").readline()

# for i in s:
#     if i == "A" and flag_A == False:
#         flag_A = True

#     if flag_A == True:
#         k += 1

#     if i == "F" and flag_A == True:
#         if 7 <= k <= 10:
#             K += 1
#         flag_A = False
#         k = 0
#         count_A = 0
# print(K)

s = open("24 (11).txt").readline()
k = 0

for i in range(len(s) - 6):
    if s[i] == "A" and s[i + 6] == "F":
        k += 1
for i in range(len(s) - 7):
    if s[i] == "A" and s[i + 7] == "F":
        k += 1
for i in range(len(s) - 8):
    if s[i] == "A" and s[i + 8] == "F":
        k += 1
for i in range(len(s) - 9):
    if s[i] == "A" and s[i + 9] == "F":
        k += 1
print(k)
